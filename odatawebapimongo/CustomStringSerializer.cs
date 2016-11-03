using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Web;
using MongoDB.Bson;
using MongoDB.Bson.Serialization;
using MongoDB.Bson.Serialization.Serializers;
using odatawebapimongo.Models;

namespace odatawebapimongo
{
    public class CustomStringSerializer:StringSerializer
    {
        public override void Serialize(BsonSerializationContext context, BsonSerializationArgs args, string value)
        {
            //switch (context.Writer.type
            //    case BsonType.Null:
            //        context.Reader.ReadNull();
            //        return null;
            //    case BsonType.String:
            //        return context.Reader.ReadString();
            //    case BsonType.Int32:
            //        return context.Reader.ReadInt32().ToString(CultureInfo.InvariantCulture);
            //    case BsonType.Int64:
            //        return context.Reader.ReadInt64().ToString(CultureInfo.InvariantCulture);
            //    default:
            //        var message = string.Format("Cannot deserialize BsonString or BsonInt32 from BsonType {0}.", context.Reader.CurrentBsonType);
            //        throw new BsonSerializationException(message);
            //}
            base.Serialize(context, args, value);
        }

        public override string Deserialize(BsonDeserializationContext context, BsonDeserializationArgs args)
        {
            //var bsonType = context.;
            switch (context.Reader.CurrentBsonType)
            {
                case BsonType.Null:
                    context.Reader.ReadNull();
                    return null;
                case BsonType.String:
                    return context.Reader.ReadString();
                case BsonType.Int32:
                    return context.Reader.ReadInt32().ToString(CultureInfo.InvariantCulture);
                case BsonType.Int64:
                    return context.Reader.ReadInt64().ToString(CultureInfo.InvariantCulture);
                default:
                    var message = string.Format("Cannot deserialize BsonString or BsonInt32 from BsonType {0}.", context.Reader.CurrentBsonType);
                    throw new BsonSerializationException(message);
            }
            return base.Deserialize(context, args);
        }
    }
}