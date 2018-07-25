import org.apache.spark.SparkContext

import scala.collection.mutable.ListBuffer
import scala.util.parsing.json.JSONObject

/**
  * Created by YGYG on 2018/7/20.
  */
object Gaokaoxx {
  def main(args: Array[String]) {
    val xml = <ul class="clearfix">
      <li data-val="北京" data-id="2" onclick="$.setVar('claimCity', 11)">北京</li>
      <li data-val="天津" data-id="2" onclick="$.setVar('claimCity', 12)">天津</li>
      <li data-val="河北" data-id="2" onclick="$.setVar('claimCity', 13)">河北</li>
      <li data-val="山西" data-id="2" onclick="$.setVar('claimCity', 14)">山西</li>
      <li data-val="内蒙古" data-id="2" onclick="$.setVar('claimCity', 15)">内蒙古</li>
      <li data-val="辽宁" data-id="2" onclick="$.setVar('claimCity', 21)">辽宁</li>
      <li data-val="吉林" data-id="2" onclick="$.setVar('claimCity', 22)">吉林</li>
      <li data-val="黑龙江" data-id="2" onclick="$.setVar('claimCity', 23)">黑龙江</li>
      <li data-val="上海" data-id="2" onclick="$.setVar('claimCity', 31)">上海</li>
      <li data-val="江苏" data-id="2" onclick="$.setVar('claimCity', 32)">江苏</li>
      <li data-val="浙江" data-id="2" onclick="$.setVar('claimCity', 33)">浙江</li>
      <li data-val="安徽" data-id="2" onclick="$.setVar('claimCity', 34)">安徽</li>
      <li data-val="福建" data-id="2" onclick="$.setVar('claimCity', 35)">福建</li>
      <li data-val="江西" data-id="2" onclick="$.setVar('claimCity', 36)">江西</li>
      <li data-val="山东" data-id="2" onclick="$.setVar('claimCity', 37)">山东</li>
      <li data-val="河南" data-id="2" onclick="$.setVar('claimCity', 41)">河南</li>
      <li data-val="湖北" data-id="2" onclick="$.setVar('claimCity', 42)">湖北</li>
      <li data-val="湖南" data-id="2" onclick="$.setVar('claimCity', 43)">湖南</li>
      <li data-val="广东" data-id="2" onclick="$.setVar('claimCity', 44)">广东</li>
      <li data-val="广西" data-id="2" onclick="$.setVar('claimCity', 45)">广西</li>
      <li data-val="海南" data-id="2" onclick="$.setVar('claimCity', 46)">海南</li>
      <li data-val="重庆" data-id="2" onclick="$.setVar('claimCity', 50)">重庆</li>
      <li data-val="四川" data-id="2" onclick="$.setVar('claimCity', 51)">四川</li>
      <li data-val="贵州" data-id="2" onclick="$.setVar('claimCity', 52)">贵州</li>
      <li data-val="云南" data-id="2" onclick="$.setVar('claimCity', 53)">云南</li>
      <li data-val="西藏" data-id="2" onclick="$.setVar('claimCity', 54)">西藏</li>
      <li data-val="陕西" data-id="2" onclick="$.setVar('claimCity', 61)">陕西</li>
      <li data-val="甘肃" data-id="2" onclick="$.setVar('claimCity', 62)">甘肃</li>
      <li data-val="青海" data-id="2" onclick="$.setVar('claimCity', 63)">青海</li>
      <li data-val="宁夏" data-id="2" onclick="$.setVar('claimCity', 64)">宁夏</li>
      <li data-val="新疆" data-id="2" onclick="$.setVar('claimCity', 65)">新疆</li>
    </ul>
    xml.child.foreach(node=>{
      val value = node.attribute("onclick")
      if (value!=None){
        val a = value.get.toString().split(", ")(1).substring(0,2)
        println(a)
      }
    })
  }

}
/**
  * 1.读取文件textFile
  * 2.过滤"status":0}的数据 filter
  * 3.将 "data":Array[5]转变成多行  flatMap   抚平
  * 4.获取 "school":"华南师范大学",  "plan":"2",
  * 4.获取 "school":"华南师范大学",  "plan":"2",  reduce 缩减
  * 5.学校和招生人数 排序， 按照招生人数排序 。sort
  *
  */
object YaSpark1{
  def main(args: Array[String]) {
    import org.json.JSONObject//导入str转json工具包
    import org.apache.spark.SparkConf//
    import org.apache.spark.SparkContext
    //sparkcontext的配置，运行在本地，名称为cala
    val conf = new SparkConf().setAppName("cala").setMaster("local").set("spark.testing.memory","2147480000")
    val sc = new SparkContext(conf)//Spark运行环境,,本地电脑，集群
    //使用spark读取文本文件
    sc.textFile("E:\\大数据\\第三组黑吉上数据.txt")
      .filter(line=>line.endsWith("status\":1}"))
      .flatMap(line=>{//line str===>List line  抚平
      val  json = new JSONObject(line)
        val jsonlist = json.getJSONArray("data")
        //        jsonlist.getJSONObject(0)
        val list = ListBuffer[JSONObject]()
        for(i<-0 to jsonlist.length()-1){
          list.append(jsonlist.getJSONObject(i))
        }
        list
      })
      .map(line=>(line.getString("school"),line.getString("plan").toInt))
      .reduceByKey(_+_)
      .foreach(line=>println(line))
    val getSchool = new Array[String]()
  }
}
object YaSparkTest{
  def main(args: Array[String]) {
    println("aaa@qq.com".endsWith("qq.com"))
    println("status\":1}")
    //    new JsonObject
    //    import json    将字符串转换为json（字典）
    import org.json.JSONObject
    val json = new JSONObject("{\"data\":{\"city_name\":\"\\u6e56\\u5357\"},\"info\":\"\",\"status\":0}")
    println(json.getInt("status"))
    println(json.getJSONObject("data"))
    val list = List[Int](1,1,1)//大小不变的固定列表
    //    list(2) = 3
    val list2 = ListBuffer[Int]()
    list2.append(3)
    list2.append(4)
    println(list2)
  }
}



