import mysql.connector
import mysql.connector.pooling
import pandas as pd
from tqdm import tqdm
import os, re, json, sys, traceback, time


# 保存错误日志至文件中
def saveErrorLog(msg):
    try:
        path = os.getcwd()
        filePath = path + os.sep + "CheckDBErrorLog.txt"
        with open(filePath, 'a+', encoding='utf-8') as f:
            f.writelines(msg + "\n")
        f.close()
    except Exception as e:
        if 'f' in dir():
            f.close()
        traceback.print_exc()
        print("ERROR:信息保存出错，信息为：" + msg)


# 保存运行日志至文件中
def saveLog(msg):
    try:
        path = os.getcwd()
        filePath = path + os.sep + "CheckDBLog.txt"
        with open(filePath, 'a+', encoding='utf-8') as f:
            f.writelines(msg + "\n")
        f.close()
    except Exception as e:
        if 'f' in dir():
            f.close()
        traceback.print_exc()
        print("ERROR:信息保存出错，信息为：" + msg)


# 读取配置文件
def getDBConfig(DBConfig):
    data = dict()
    try:
        with open(DBConfig, 'r', encoding='utf-8') as f:
            data = json.load(f)
        f.close()
    except Exception as e:
        if 'f' in dir():
            f.close()
            saveAndPrintERROR("ERROR:读取数据库配置文件出错")
            saveLog("ERROR:读取数据库配置文件出错")
        traceback.print_exc()
    return data


# 打印错误信息并保存在日志文件中
def saveAndPrintERROR(msg):
    print(msg)
    saveErrorLog(msg)


# 通过excel生成view名与prikey信息的json文件
# 所有view删去batch_no主键
def getKeysFromExcel(excelName, sheetName, columns, interfaceCName):
    viewAndKeys = dict()
    data = pd.read_excel(excelName, sheetName, usecols=columns)
    viewName = ""
    for i in tqdm(range(len(data.values)), desc='excel处理', unit='条'):
        if isinstance(data.values[i][0], str) and data.values[i][0].strip() == interfaceCName:
            viewName = data.values[i][1].split('|')[0].strip()
        if isinstance(data.values[i][2], str) and data.values[i][2].strip() == 'Y':
            if data.values[i][1].strip() != "batch_no":
                if viewName not in viewAndKeys:
                    viewAndKeys[viewName] = data.values[i][1].strip()
                else:
                    viewAndKeys[viewName] += '|' + data.values[i][1].strip()
    jsonName = excelName[:-5] + sheetName + ".json"
    try:
        with open(jsonName, 'w', encoding='utf-8') as f:
            json.dump(viewAndKeys, f, indent=4)
            f.close()
    except Exception as e:
        if 'f' in dir():
            f.close()
        saveAndPrintERROR("ERROR:生成视图名与主键文件失败")
        saveLog("ERROR:生成视图名与主键文件失败")
        traceback.print_exc()
    return jsonName


# 获取view名与prikey信息
def getViewAndKeys(filePath):
    try:
        with open(filePath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        f.close()
    except Exception as e:
        if 'f' in dir():
            f.close()
            saveAndPrintERROR("ERROR:读取视图与主键json出错")
            saveLog("ERROR:读取视图与主键json出错")
        traceback.print_exc()
    for key, value in data.items():
        priKey = value.split('|')
        data[key] = priKey
    return data


# 获取指定数据库的所有view名，返回为list
def findViewName(pool, dbName):
    viewName = []
    try:
        con = pool.get_connection()
        cursor = con.cursor()
        sql = "SELECT TABLE_NAME FROM information_schema.`TABLES` a WHERE a.TABLE_SCHEMA= %s AND a.TABLE_TYPE='view';"
        cursor.execute(sql, (dbName,))
        for itor in cursor:
            viewName.append(itor[0])
        con.close()
    except Exception as e:
        if "con" in dir():
            con.close()
        saveAndPrintERROR("ERROR:获取当前数据库:" + dbName + "所有视图名称出错")
        saveLog("ERROR:获取当前数据库:" + dbName + "所有视图名称出错")
        traceback.print_exc()
    return viewName


# 获取指定数据库中指定view中的字段名，返回list
def getColumnsFromView(pool, dbName, viewName):
    columns = []
    try:
        con = pool.get_connection()
        cursor = con.cursor()
        sql = "SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME=%s AND TABLE_SCHEMA=%s ;"
        cursor.execute(sql, (viewName, dbName))
        for itor in cursor:
            columns.append(itor)
        con.close()
    except Exception as e:
        if "con" in dir():
            con.close()
        saveAndPrintERROR("ERROR:当前视图" + viewName + "字段信息获取失败")
        saveLog("ERROR:当前视图" + viewName + "字段信息获取失败")
        traceback.print_exc()
    return columns


# 获取指定数据库中指定视图中的字段及其类型，返回list
def getColumnsInfoFromView(pool, dbName, viewName):
    columns = []
    try:
        con = pool.get_connection()
        cursor = con.cursor()
        sql = "SELECT COLUMN_NAME,COLUMN_TYPE FROM information_schema.COLUMNS WHERE TABLE_NAME=%s AND TABLE_SCHEMA=%s;"
        cursor.execute(sql, (viewName, dbName))
        for itor in cursor:
            columns.append(itor)
        con.close()
    except Exception as e:
        if "con" in dir():
            con.close()
        saveAndPrintERROR("ERROR:获取当前视图" + viewName + "字段名与类型失败")
        saveLog("ERROR:获取当前视图" + viewName + "字段名与类型失败")
        traceback.print_exc()
    return columns


# 获取视图对应的信息
def getDataFromView(pool, dbName, viewName):
    result = []
    try:
        con = pool.get_connection()
        cursor = con.cursor()
        sql = "SELECT * FROM " + dbName + "." + viewName + ";"
        cursor.execute(sql)
        for itor in tqdm(cursor, desc=viewName + '获取数据', unit='条'):
            result.append(itor)
        con.close()
    except Exception as e:
        if "con" in dir():
            con.close()
        saveAndPrintERROR("ERROR:当前视图" + viewName + "信息获取失败")
        saveLog("ERROR:当前视图" + viewName + "信息获取失败")
        traceback.print_exc()
    return result


# 检查两个数据库中同名视图中字段差异信息，返回两个库里同名字段
def checkViewBetweenOldAndNew(oldPool, newPool, dbNameOld, dbNameNew):
    # 获取新旧数据库中同名视图
    viewNameOld = findViewName(oldPool, dbNameOld)
    viewNameNew = findViewName(newPool, dbNameNew)
    sameView = set(viewNameOld) & set(viewNameNew)
    diffView = set()
    # 对比每个同名视图中的字段信息
    for view in sameView:
        oldColumn = getColumnsFromView(oldPool, dbNameOld, view)
        newColumn = getColumnsFromView(newPool, dbNameNew, view)
        diff = set(oldColumn) ^ set(newColumn)
        if diff:
            msg = "新视图中字段少于对应旧视图，该视图为：" + view + "\n差异字段共有" + str(len(diff)) + "个，展示如下：\n"
            for itor in diff:
                msg += itor[0] + "\n"
            saveAndPrintERROR(msg)
            saveLog(msg)
            diffView.add(view)
        else:
            msg = "视图名：" + view + "在新旧数据库中字段一致\n"
            saveLog(msg)
    return sameView - diffView


# 检查两个数据库中数据是否完全相同
def checkDataBetweenOldAndNew(oldPool, newPool, dbNameOld, dbNameNew, sameView):
    for view in sameView:
        oldData = getDataFromView(oldPool, dbNameOld, view)
        newData = getDataFromView(newPool, dbNameNew, view)
        oldHaveNewNot = [x for x in oldData if x not in newData]
        newHaveOldNot = [x for x in newData if x not in oldData]
        # todo


# 返回数据库中所有数据库名称
def getDBName(pool):
    dbName = set()
    try:
        con = pool.get_connection()
        cursor = con.cursor()
        cursor.execute("SHOW DATABASES;")
        for itor in cursor:
            dbName.add(itor[0])
        con.close()
    except Exception as e:
        if "con" in dir():
            con.close()
        saveAndPrintERROR("ERROR:获取当前数据库中所有数据库信息失败")
        saveLog("ERROR:获取当前数据库中所有数据库信息失败")
        traceback.print_exc()
    return dbName


# 返回指定数据库中所有表名称包括视图
def getTableAndViewName(pool, dbName):
    tableAndViewName = set()
    try:
        con = pool.get_connection()
        cursor = con.cursor()
        sql = "SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA=%s;"
        cursor.execute(sql, (dbName,))
        for itor in cursor:
            tableAndViewName.add(itor[0])
        con.close()
    except Exception as e:
        if "con" in dir():
            con.close()
        saveAndPrintERROR("ERROR:获取数据库中所有表与视图名称失败")
        saveLog("ERROR:获取数据库中所有表与视图名称失败")
        traceback.print_exc()
    return tableAndViewName


# 返回指定数据库中的虽有视图名称
def getViewName(pool, dbName):
    viewName = set()
    try:
        con = pool.get_connection()
        cursor = con.cursor()
        sql = "SELECT TABLE_NAME FROM information_schema.VIEWS WHERE TABLE_SCHEMA=%s;"
        cursor.execute(sql, (dbName,))
        for itor in cursor:
            viewName.add(itor[0])
        con.close()
    except Exception as e:
        if "con" in dir():
            con.close()
        saveAndPrintERROR("ERROR:获取数据库中所有视图名称失败")
        saveLog("ERROR:获取数据库中所有视图名称失败")
        traceback.print_exc()
    return viewName


# 返回指定数据库中所有表名称不包括视图
# todo 这里可以改成直接使用sql
def getTableName(pool, dbName):
    tableAndViewName = getTableAndViewName(pool, dbName)
    viewName = getViewName(pool, dbName)
    tableName = tableAndViewName - viewName
    return tableName


# 返回整个数据库Map信息，key为数据库名，value为数据库中所有表名称
def getDBMap(pool):
    DBMap = dict()
    dbList = getDBName(pool)
    for itor in dbList:
        DBMap[itor] = getTableName(pool, itor)
    return DBMap


# 返回view所用的数据表使用正则提取sql中的数据表名称 暂时弃用
def getTableFromViewByRe(pool):
    try:
        con = pool.get_connection()
        cursor = con.cursor()
        con.close()
    except Exception as e:
        if "con" in dir():
            con.close()
        traceback.print_exc()
    sql = "SELECT TABLE_SCHEMA,VIEW_DEFINITION FROM information_schema.VIEWS;"
    ruleFrom = r'from (.*)'
    sqlFrom = re.findall(ruleFrom, sql)[0]
    ruleCut = r'.`(.*?)`'
    cut = set(re.findall(ruleCut, sqlFrom))
    # todo


# 获取对应数据库中视图的字段及其位置，返回key为列名，value为位置
def getColumnAndPosition(pool, dbName, viewName):
    columnPositionMap = dict()
    try:
        con = pool.get_connection()
        cursor = con.cursor()
        sql = "SELECT COLUMN_NAME,ORDINAL_POSITION FROM information_schema.COLUMNS " \
              "WHERE TABLE_NAME=%s AND TABLE_SCHEMA=%s ORDER BY ORDINAL_POSITION;"
        cursor.execute(sql, (viewName, dbName))
        for itor in cursor:
            columnPositionMap[itor[0]] = itor[1]
        con.close()
    except Exception as e:
        if "con" in dir():
            con.close()
        saveAndPrintERROR("ERROR:获取数据库中" + viewName + "视图的字段及其位置失败")
        saveLog("ERROR:获取数据库中" + viewName + "视图的字段及其位置失败")
        traceback.print_exc()
    return columnPositionMap


# 利用旧数据库中视图在新数据库同名数据库下创建表
# 返回list，[0]为完整表名，[1:]为列名
def createNewTableFromViewToNewDB(oldPool, newPool, dbNameOld, dbNameNew, viewName):
    tableName = dbNameNew + ".test_" + viewName
    tableInfo = [tableName, ]
    columns = getColumnsInfoFromView(oldPool, dbNameOld, viewName)
    structTable = "("
    for column in columns:
        structTable += " " + column[0] + " " + column[1] + " ,"
        tableInfo.append(column[0])
    structTable = structTable[:-1] + ")"
    try:
        con = newPool.get_connection()
        con.start_transaction()
        cursor = con.cursor()
        cursor.execute("DROP TABLE IF EXISTS " + tableName)
        cursor.execute("CREATE TABLE IF NOT EXISTS " + tableName + " " + structTable)
        con.commit()
        con.close()
    except Exception as e:
        if "con" in dir():
            con.rollback()
            con.close()
        saveAndPrintERROR("ERROR:新表" + tableName + "创建失败")
        saveLog("ERROR:新表" + tableName + "创建失败")
        traceback.print_exc()
    return tableInfo


# 将旧数据库中视图对应数据插入到新数据库中
def insertDataToNewTable(pool, tableInfo, data):
    insertSQL = "INSERT INTO " + tableInfo[0] + " ("
    for column in tableInfo[1:]:
        insertSQL += column + ", "
    insertSQL = insertSQL[:-2] + ") VALUES ( "
    for i in range(len(tableInfo) - 1):
        insertSQL += "%s, "
    insertSQL = insertSQL[:-2] + ")"
    try:
        con = pool.get_connection()
        con.start_transaction()
        cursor = con.cursor()
        cursor.executemany(insertSQL, tqdm(data, desc=tableInfo[0] + '插入数据', unit='条'))
        con.commit()
        con.close()
    except Exception as e:
        if "con" in dir():
            con.rollback()
            con.close()
        saveAndPrintERROR("ERROR:数据表" + tableInfo[0] + "插入数据失败")
        saveLog("ERROR:数据表" + tableInfo[0] + "插入数据失败")
        traceback.print_exc()


# 查找旧数据库中存在且新数据库中不存在的记录，返回查找SQL和符合条件的记录条数
def findDiffInOldView(pool, oldTableName, newViewName, priKey):
    result = []
    onSQL = ""
    whereSQL = ""
    for key in priKey:
        onSQL += "old." + key + "=new." + key + " AND "
        whereSQL += "new." + key + " IS NULL AND "
    onSQL = onSQL[:-4]
    whereSQL = whereSQL[:-4]
    sql = "SELECT old.* FROM " + oldTableName + " old LEFT JOIN " + newViewName \
          + " new ON " + onSQL + " WHERE " + whereSQL + ";"
    countSQL = "SELECT COUNT(*) FROM " + oldTableName + " old LEFT JOIN " + newViewName \
               + " new ON " + onSQL + " WHERE " + whereSQL + ";"
    result.append(sql)
    try:
        con = pool.get_connection()
        cursor = con.cursor()
        cursor.execute(countSQL)
        for item in cursor:
            num = item[0]
        result.append(num)
        con.close()
    except Exception as e:
        if "con" in dir():
            con.close()
        saveAndPrintERROR("ERROR:检查视图" + newViewName + "旧数据库独有记录出错")
        saveLog("ERROR:检查视图" + newViewName + "旧数据库独有记录出错")
        traceback.print_exc()
    return result


# 查找新数据库中存在且旧数据库中不存在的记录，返回查找SQL和符合条件的记录条数
def findDiffInNewView(pool, oldTableName, newViewName, priKey):
    result = []
    onSQL = ""
    whereSQL = ""
    for key in priKey:
        onSQL += "old." + key + "=new." + key + " AND "
        whereSQL += "old." + key + " IS NULL AND "
    onSQL = onSQL[:-4]
    whereSQL = whereSQL[:-4]
    sql = "SELECT new.* FROM " + oldTableName + " old RIGHT JOIN " + newViewName \
          + " new ON " + onSQL + " WHERE " + whereSQL + ";"
    countSQL = "SELECT COUNT(*) FROM " + oldTableName + " old RIGHT JOIN " + newViewName \
               + " new ON " + onSQL + " WHERE " + whereSQL + ";"
    result.append(sql)
    try:
        con = pool.get_connection()
        cursor = con.cursor()
        cursor.execute(countSQL)
        for item in cursor:
            num = item[0]
        result.append(num)
        con.close()
    except Exception as e:
        if "con" in dir():
            con.close()
        saveAndPrintERROR("ERROR:检查视图" + newViewName + "新数据库独有记录出错")
        saveLog("ERROR:检查视图" + newViewName + "新数据库独有记录出错")
        traceback.print_exc()
    return result


# 查找旧数据库中存在且新数据库中存在但不同的记录，返回查找SQL和符合条件的记录条数
def findDiffBetweenOldAndNew(pool, oldTableName, newViewName, priKey, keys):
    result = []
    showSQL = ""
    onSQL = ""
    for key in priKey:
        onSQL += "old." + key + "=new." + key + " AND "
        showSQL += "old." + key + ",new." + key + ","
    onSQL = onSQL[:-4]
    if keys != []:
        orSQL = " AND ( "
        for key in keys:
            orSQL += "old." + key + "!=new." + key + " OR "
            showSQL += "old." + key + ",new." + key + ","
        orSQL = orSQL[:-3] + ")"
    else:
        orSQL = ""
    showSQL = showSQL[:-1]
    sql = "SELECT " + showSQL + " FROM " + oldTableName + " old INNER JOIN " + newViewName \
          + " new ON " + onSQL + orSQL + ";"
    countSQL = "SELECT COUNT(*) FROM " + oldTableName + " old INNER JOIN " + newViewName \
               + " new ON " + onSQL + orSQL + ";"
    result.append(sql)
    try:
        con = pool.get_connection()
        cursor = con.cursor()
        cursor.execute(countSQL)
        for item in cursor:
            num = item[0]
        result.append(num)
        con.close()
    except Exception as e:
        if "con" in dir():
            con.close()
        saveAndPrintERROR("ERROR:检查视图" + newViewName + "新旧数据库共有记录差异出错")
        saveLog("ERROR:检查视图" + newViewName + "新旧数据库共有记录差异出错")
        traceback.print_exc()
    return result


# 给指定数据库添加主键索引
def setPriIndexForTable(pool, tableName, priKey):
    keys = ""
    for key in priKey:
        keys += key + ','
    keys = keys[:-1]
    sql = "ALTER TABLE " + tableName + " ADD PRIMARY KEY ( " + keys + " );"
    try:
        con = pool.get_connection()
        con.start_transaction()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()
    except Exception as e:
        if "con" in dir():
            con.rollback()
            con.close()
        saveAndPrintERROR("ERROR:数据表" + tableName + "设置主键出错，可能存在主键重复的情况，请排查。\n设置主键sql为：" + sql)
        saveLog("ERROR:数据表" + tableName + "设置主键出错，可能存在主键重复的情况，请排查。\n设置主键sql为：" + sql)
        traceback.print_exc()


# 对比view数据之间的差异，返回格式为list，其数据格式如下：
# diff[0]表示旧数据库比新数据库多的信息
# diff[1]表示新数据库比旧数据库多的信息
# diff[2]表示两个数据库都存在的信息但不同的信息
def checkDataDiffBetweenDBs(oldPool, newPool, dbNameOld, dbNameNew, viewName, priKey):
    diff = [None] * 3
    # 将旧数据库中的视图数据迁移至新数据库中并生成test_+view名的数据表
    oldData = getDataFromView(oldPool, dbNameOld, viewName)
    tableInfo = createNewTableFromViewToNewDB(oldPool, newPool, dbNameOld, dbNameNew, viewName)
    insertDataToNewTable(newPool, tableInfo, oldData)
    oldViewName = tableInfo[0]
    newViewName = dbNameNew + "." + viewName
    # 给新建的创建主键索引
    setPriIndexForTable(newPool, oldViewName, priKey)
    # 找出所有非主键列名
    keys = []
    for item in tableInfo[1:]:
        if item not in priKey:
            keys.append(item)
    diff[0] = findDiffInOldView(newPool, oldViewName, newViewName, priKey)
    diff[1] = findDiffInNewView(newPool, oldViewName, newViewName, priKey)
    diff[2] = findDiffBetweenOldAndNew(newPool, oldViewName, newViewName, priKey, keys)
    if diff[0][1]:
        msg = "视图： " + newViewName + " 中共有" + str(diff[0][1]) + "条记录只在旧数据库中\n查询SQL为： " + diff[0][0] + "\n"
        saveAndPrintERROR(msg)
        saveLog(msg)
    else:
        msg = "视图： " + newViewName + "在旧数据库中无独有数据\n"
        saveLog(msg)
    if diff[1][1]:
        msg = "视图： " + newViewName + " 中共有" + str(diff[1][1]) + "条记录只在新数据库中\n查询SQL为： " + diff[1][0] + "\n"
        saveAndPrintERROR(msg)
        saveLog(msg)
    else:
        msg = "视图： " + newViewName + "在新数据库中无独有数据\n"
        saveLog(msg)
    if diff[2][1]:
        msg = "视图： " + newViewName + " 中共有" + str(diff[2][1]) + "条记录存在新旧数据库中但记录不同\n查询SQL为： " + diff[2][0] + "\n"
        saveAndPrintERROR(msg)
        saveLog(msg)
    else:
        msg = "视图： " + newViewName + "在新旧数据库中一致\n"
        saveLog(msg)
    return diff


# 删除临时创建的表
def removeTempTable(pool, tableName):
    try:
        con = pool.get_connection()
        con.start_transaction()
        cursor = con.cursor()
        cursor.execute("DROP TABLE " + tableName)
        con.commit()
        con.close()
    except Exception as e:
        if "con" in dir():
            con.rollback()
            con.close()
        saveAndPrintERROR("ERROR:删除临时表" + tableName + "失败")
        saveLog("ERROR:删除临时表" + tableName + "失败")
        traceback.print_exc()


# 显示差异数据明细
def showData(data, tableInfo):
    for column in tableInfo[1:]:
        print(column + "\t\t", end="")
    print("表名")
    columns = ""
    for item in tableInfo[1:]:
        columns += item + "\t\t"
    saveLog(columns + "表名")
    for i in range(len(data)):
        info = ""
        for j in range(len(data[i])):
            if isinstance(data[i][j], bytearray):
                data[i][j] = data[i][j].decode('utf-8')
            print(str(data[i][j]), end="\t\t")
            info += str(data[i][j]) + "\t\t"
        saveLog(info)
        print()


# 比较view数据之间的差异，并打印与把保存每条差异数据，并删除临时表
def checkDataDiffDetailBetweenDBs(oldPool, newPool, dbNameOld, dbNameNew, viewName, priKey):
    data = []
    # 将旧数据库中的视图数据迁移至新数据库中并生成test_+view名的数据表
    oldData = getDataFromView(oldPool, dbNameOld, viewName)
    tableInfo = createNewTableFromViewToNewDB(oldPool, newPool, dbNameOld, dbNameNew, viewName)
    insertDataToNewTable(newPool, tableInfo, oldData)
    columns = ""
    for column in tableInfo[1:]:
        columns += column + ","
    columns = columns[:-1]
    keys = ""
    for key in priKey:
        keys += key + ","
    keys = keys[:-1]
    sql = "SELECT * FROM " \
          "(SELECT *,%s as table_name FROM " + tableInfo[0] + \
          " UNINO ALL SELECT *,%s as table_name FROM " + dbNameNew + "." + viewName + ") tbl " \
                                                                                      "GROUP BY " + columns + " HAVING COUNT(*)=1 ORDER BY " + keys + ";"
    try:
        con = newPool.get_connection()
        cursor = con.cursor()
        cursor.execute(sql, ("old_" + viewName, "new_" + viewName))
        for itor in cursor:
            item = []
            for it in itor:
                item.append(it)
            data.append(item)
        con.close()
    except Exception as e:
        if "con" in dir():
            con.close()
        saveAndPrintERROR("ERROR:对比过程出错")
        saveLog("ERROR:对比过程出错")
        traceback.print_exc()
    removeTempTable(newPool, tableInfo[0])
    # 显示差异数据明细，暂不显示，改显示SQL，统计差异条数
    showData(data, tableInfo)


# 检查json文件中配置的所有view
def checkAllView(oldPool, newPool, dbNameOld, dbNameNew, viewAndKeys):
    for key, value in viewAndKeys.items():
        start = time.time()
        checkDataDiffBetweenDBs(oldPool, newPool, dbNameOld, dbNameNew, key, value)
        end = time.time()
        speedTime = str(end - start)
        print("视图：" + key + "花费时间为：" + speedTime + "秒")
        saveLog("视图：" + key + "花费时间为：" + speedTime + "秒\n\n")
        # 该方法会显示数据差异明细并保存在文件中并删除临时表
        # checkDataDiffDetailBetweenDBs(oldPool,newPool,dbNameOld,dbNameNew,key,value)


if __name__ == '__main__':
    start = time.time()
    jsonName = getKeysFromExcel("可用风控中心交互接口-202001.00.xlsm", "日初基础视图", [1, 2, 6], "接口名称")
    # todo 读取命令行参数
    # 第一个为固定参数，用来接收数据库配置信息
    # 第二个为可变参数，用来接收视图与逐渐关系
    if sys.argv[1:] == []:
        print("未指定指定配置文件，执行默认逻辑")
        dbConfigName = os.getcwd() + os.sep + "DBConfig.json"
    else:
        dbConfigName = sys.argv[1]
        viewAndKeys = sys.argv[2:]
    dbConfig = getDBConfig(dbConfigName)
    oldDB = dbConfig["oldDB"]
    newDB = dbConfig["newDB"]
    dbNameOld = oldDB["database"]
    dbNameNew = newDB["database"]
    viewAndKeys = getViewAndKeys(jsonName)
    try:
        # 创建数据库连接池，优化查询IO性能
        oldPool = mysql.connector.pooling.MySQLConnectionPool(**oldDB, pool_size=2)
        newPool = mysql.connector.pooling.MySQLConnectionPool(**newDB, pool_size=2)
        # 此函数对应功能二
        sameNameAndColumnsView = checkViewBetweenOldAndNew(oldPool, newPool, dbNameOld, dbNameNew)
        # 筛去数据库中没有但excel中有或字段不同的视图名
        for view in list(viewAndKeys.keys()):
            if view not in sameNameAndColumnsView:
                viewAndKeys.pop(view)
        # 此函数对应功能一
        checkAllView(oldPool, newPool, dbNameOld, dbNameNew, viewAndKeys)
    except Exception as e:
        traceback.print_exc()
    end = time.time()
    timeMin = int((end - start) % 60)
    timeHour = int((end - start) / 60)
    print("完成，花费时间：" + str(timeHour) + "分" + str(timeMin) + "秒")
