1. 什么是索引

    索引就是对数据库里表的一列或多列值进行排序的结构，相当于目录和正文内容的关系，可以提高查询效率。

2. 如何创建索引

    - 普通索引，没有唯一性限制

        `ALTER TABLE table_name ADD INDEX index_name(column1, column2, column3)`
    
    - 唯一索引
    
        `ALTER TABLE table_name ADD UNIQUE (column1, column2)`
        
3. 索引创建原则

    - 主键和外键一定要建立索引
    
    - 经常查询的数据列最好建立索引
    
    - where子句中常用的列要建立索引
    
    - 经常出现在groub by、order by、distinct后面的列要建立索引
    
    - 经常用作表连接的字段