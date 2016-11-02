using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace odatawebapimongo.Models
{
    [BsonIgnoreExtraElements]
    public class SubItem
    {
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        public string Id { get; set; }

        [BsonElement("FRN")]
        public int Frn { get; set; }

        [BsonElement("Orig R Annual Cost")]
        public string OrigRAnnualCost { get; set; }
    }
}