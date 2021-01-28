using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        static void move()
        {
            var httpWebRequest = (HttpWebRequest)WebRequest.Create("http://31.16.40.112:8888/");
            httpWebRequest.ContentType = "application/json";
            httpWebRequest.Method = "POST";

            Random _random = new Random();

            using (var streamWriter = new StreamWriter(httpWebRequest.GetRequestStream()))
            {
                Class1 test = new Class1();
                test.X = _random.Next(0, 180);
                test.Y = _random.Next(0, 180);
                test.ON = true;

                string json = JsonConvert.SerializeObject(test);
                Console.WriteLine(json);

                streamWriter.Write(json);
            }
            var httpResponse = (HttpWebResponse)httpWebRequest.GetResponse();
            using (var streamReader = new StreamReader(httpResponse.GetResponseStream()))
            {
                var result = streamReader.ReadToEnd();
            }
        }

        static void Main(string[] args)
        {
            while (true)
            {
                move();
            }
        }
    }
}
