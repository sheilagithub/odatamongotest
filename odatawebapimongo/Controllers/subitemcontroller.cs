using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Http;
using System.Web.OData;
using MongoDB.Bson;
using MongoDB.Driver;
using MongoDB.Driver.Linq;
using odatawebapimongo.Models;

namespace odatawebapimongo.Controllers
{

    public class subitemcontroller : ODataController
    {

        private MongoClient _client;
        private IMongoDatabase _db;


        public subitemcontroller()
        {
            _client = new MongoClient("mongodb://eratedemo:eratedemo@ds057934.mlab.com:57934/eratedemo");
            _db = _client.GetDatabase("eratedemo");
        }

        [EnableQuery]
        public IQueryable<SubItem> Get()
        {
            var collection = _db.GetCollection<SubItem>("applications");
            return collection.AsQueryable();
        }

        [System.Web.Http.OData.EnableQuery]
        public SingleResult<SubItem> Get([System.Web.Http.OData.FromODataUri] string key)
        {
            var application =
                     _db.GetCollection<SubItem>("applications").AsQueryable().Where(e => e.Id == key);

            return SingleResult.Create(application);
        }
    }
}