using System;
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

    public class ProductsController : ODataController
    {
        private MongoClient _client;
        private IMongoDatabase _db;

        public ProductsController()
        {
            _client = new MongoClient("mongodb://eratedemo:eratedemo@ds057934.mlab.com:57934/eratedemo");
            _db = _client.GetDatabase("eratedemo");
            InitDatabase();

        }

        [EnableQuery]
        public IQueryable<Product> Get()
        {

            var products = _db.GetCollection<Product>("products").Find(new BsonDocument());
            return products.ToList<Product>().AsQueryable();
        }

        [EnableQuery]
        public SingleResult<Product> Get([FromODataUri] int key)
        {
            var query = Builders<Product>.Filter.Eq(e => e.Id, key);
            var product = _db.GetCollection<Product>("products").Find(query).ToList().AsQueryable();


           
            return SingleResult.Create(product);
        }

        protected void InitDatabase()
        {

            var products = _db.GetCollection<Product>("products");
            if (products.Count(new BsonDocument()) == 0)
            {
                var p1 = new Product()
                {
                    Id = 1,
                    Name = "Bread",
                };

                var p2 = new Product()
                {
                    Id = 2,
                    Name = "Milk",
                };

                var p3 = new Product()
                {
                    Id = 3,
                    Name = "Jam",
                };

                products.InsertOne(p1);
                products.InsertOne(p2);
                products.InsertOne(p3);
            }
        }
    }
}