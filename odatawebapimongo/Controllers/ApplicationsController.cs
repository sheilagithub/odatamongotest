﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Http.OData;
using MongoDB.Bson;
using MongoDB.Driver;
using odatawebapimongo.Models;
using ODataController = System.Web.OData.ODataController;
using System.Web.Http;

namespace odatawebapimongo.Controllers
{

    public class ApplicationsController : ODataController
    {
        private MongoClient _client;
        private IMongoDatabase _db;

        public ApplicationsController()
        {
            _client = new MongoClient("mongodb://eratedemo:eratedemo@ds057934.mlab.com:57934/eratedemo");
            _db = _client.GetDatabase("eratedemo");

        }

        [EnableQuery]
        public IQueryable<BsonDocument> Get()
        {

            var applications = _db.GetCollection<BsonDocument>("applications").AsQueryable();
            return applications;
        }

        [EnableQuery]
        public SingleResult<Application> Get([FromODataUri] string key)
        {
            var application =
                     _db.GetCollection<Application>("applications").AsQueryable().Where(e => e.Id == key);

            return SingleResult.Create(application);
        }


    }
}