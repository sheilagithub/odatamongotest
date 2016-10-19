using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using MongoDB.Bson.Serialization.Attributes;

namespace odatawebapimongo.Models
{

    public class Product
    {
        [BsonElement("_id")]
        public int Id { get; set; }

        public string Name { get; set; }
    }

}