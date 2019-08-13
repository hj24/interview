1. Django的Queryset是什么，objects是什么，objects在哪里可以定义

    Queryset对应数据库中的若干条记录
    
2. model中的get和filter方法的区别

    - 注：从接收参数、返回内容和异常三个角度谈
    
    get：接受一个模型里的字段，匹配结果返回一个对象，如果不存在则报错
    
    filter：返回一个对象列表，如果记录不存在，不抛异常，返回空列表