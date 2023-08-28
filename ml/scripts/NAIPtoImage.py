#!/usr/bin/env python
##from __future__ import print_function
##from __future__ import unicode_literals
##from __future__ import division
##from __future__ import absolute_import
# *****************************************************************************
# *|  NAIPtoImage.py
# *| Requirements: Python 2.*
# *| Custom modules: nearmap
# *****************************************************************************
version = "v3.0 - DEV"
# *****************************************************************************
# *| Standard library imports
# *****************************************************************************

import os
import sys
import traceback
import gc
import math
import json
import time
import datetime
import logging
import psycopg2
from multiprocessing import Pool
from multiprocessing import log_to_stderr
# Package imports
import arcpy

# import nearmap
import config
import tkMessageBox

# create logger
logFile = os.path.dirname(os.path.abspath(__file__)) + os.sep + "NAIPtoImage.log"
logging.basicConfig(filename=logFile, filemode='a', level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger().addHandler(console)
logger = logging.getLogger()
logger.info("Logging has been initiated")

# globals
globNaipLyrFile = r'D:\Projects\WORKING\ML\imagery\NAIP_LYR\NAIP.lyr'
arcpy.env.workspace = r'D:\Projects\WORKING\ML\imagery\tmp\ESRI_Service'


# in script threadcount = 16


def run_error_message(string_message):
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    pymsg = tbinfo + "\n" + str(sys.exc_info()[0]) + ": " + str(sys.exc_info()[1])
    errorText = "\n>>> " + string_message + ": \n" + pymsg + "\n\n"
    print(errorText)
    logger.error(errorText)


def get_db_conn():
    conn = psycopg2.connect(dbname=config.iepocDB['dbname'], user=config.iepocDB['user'],
                            password=config.iepocDB['password'])
    return conn


def pull_naip_images():
    try:
        sql = """    select distinct filename,  bb_left, bb_bottom, bb_right, bb_top 
        from (
        SELECT state_code||cnty_code||'_'||parcel_id filename,
        round(st_xmin(st_envelope(geom))::DECIMAL,2) bb_left,
        round(st_ymin(st_envelope(geom))::DECIMAL,2) bb_bottom, 
        round(st_xmax(st_envelope(geom))::DECIMAL,2) bb_right,
        round(st_ymax(st_envelope(geom))::DECIMAL,2) bb_top 
        FROM metlife_parcels
        ) s"""
        loopCon = get_db_conn()
        loopCur = loopCon.cursor()
        loopCur.execute(sql)
        recordList = loopCur.fetchall()
        logger.info("Fetched all the data - starting the processing")
        p = Pool(16)
        for result in p.imap(download_image, recordList):
            logger.info("Image download result: " + result)
        logger.info("\t\tImages have been downloaded")
        tkMessageBox.showinfo("NAIP images downloaded", "API extract threads are finished")
    except:
        run_error_message("Pool manager error")


def download_image(rec):
    file_name, bb_left, bb_bottom, bb_right, bb_top = rec
    logger.info(str(file_name) + " - in process")
    outPath = file_name + ".tif"
    outExtent = str(bb_left) + " " + str(bb_bottom) + " " + str(bb_right) + " " + str(bb_top)
    try:
        # Need NO_MAINTAIN_EXTENT
        arcpy.Clip_management(globNaipLyrFile, outExtent, outPath, "#", "#", "NONE", "NO_MAINTAIN_EXTENT")
        logger.info(str(file_name) + " - has been downloaded")
        result = "success"
    except:
        result = "failure"
        run_error_message("Clipping failure with arcpy")
    return result


if __name__ == '__main__':
    try:
        pull_naip_images()
    except:
        run_error_message("Major Failure")
    finally:
        gc.collect()
