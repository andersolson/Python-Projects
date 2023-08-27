import arcpy

arcpy.env.overwriteOutput = True

print("Running: CA")
arcpy.management.Merge(r"D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\CA_Water.shp;D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\CA_Wildland.shp",
                       r"D:\Projects\WORKING\ML\vectors\National_WW\CA_WW_Merge.shp")

print("Running: FL")
arcpy.management.Merge(r"D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\FL_Water.shp;D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\FL_Wildland.shp",
                       r"D:\Projects\WORKING\ML\vectors\National_WW\FL_WW_Merge.shp")

print("Running: ID")
arcpy.management.Merge(r"D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\ID_Water.shp;D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\ID_Wildland.shp",
                       r"D:\Projects\WORKING\ML\vectors\National_WW\ID_WW_Merge.shp")

print("Running: MT")
arcpy.management.Merge(r"D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\MT_Water.shp;D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\MT_Wildland.shp",
                       r"D:\Projects\WORKING\ML\vectors\National_WW\MT_WW_Merge.shp")

print("Running: NM")
arcpy.management.Merge(r"D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\NM_Water.shp;D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\NM_Wildland.shp",
                       r"D:\Projects\WORKING\ML\vectors\National_WW\NM_WW_Merge.shp")

print("Running: NV")
arcpy.management.Merge(r"D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\NV_Water.shp;D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\NV_Wildland.shp",
                       r"D:\Projects\WORKING\ML\vectors\National_WW\NV_WW_Merge.shp")

print("Running: OK")
arcpy.management.Merge(r"D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\OK_Water.shp;D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\OK_Wildland.shp",
                       r"D:\Projects\WORKING\ML\vectors\National_WW\OK_WW_Merge.shp")

print("Running: OR")
arcpy.management.Merge(r"D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\OR_Water.shp;D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\OR_Wildland.shp",
                       r"D:\Projects\WORKING\ML\vectors\National_WW\OR_WW_Merge.shp")

print("Running: SD")
arcpy.management.Merge(r"D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\SD_Water.shp;D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\SD_Wildland.shp",
                       r"D:\Projects\WORKING\ML\vectors\National_WW\SD_WW_Merge.shp")

print("Running: TX")
arcpy.management.Merge(r"D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\TX_Water.shp;D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\TX_Wildland.shp",
                       r"D:\Projects\WORKING\ML\vectors\National_WW\TX_WW_Merge.shp")

print("Running: UT")
arcpy.management.Merge(r"D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\UT_Water.shp;D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\UT_Wildland.shp",
                       r"D:\Projects\WORKING\ML\vectors\National_WW\UT_WW_Merge.shp")

print("Running: WA")
arcpy.management.Merge(r"D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\WA_Water.shp;D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\WA_Wildland.shp",
                       r"D:\Projects\WORKING\ML\vectors\National_WW\WA_WW_Merge.shp")
print("Running: WY")
arcpy.management.Merge(r"D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\WY_Water.shp;D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\WY_Wildland.shp",
                       r"D:\Projects\WORKING\ML\vectors\National_WW\WY_WW_Merge.shp")