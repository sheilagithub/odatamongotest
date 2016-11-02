using System.Web.Http;
using System.Web.OData.Builder;
using System.Web.OData.Extensions;
using odatawebapimongo.Models;

namespace odatawebapimongo
{
    public static class WebApiConfig
    {
        public static void Register(HttpConfiguration config)
        {
            var builder = new ODataConventionModelBuilder();

            builder.EntitySet<Product>("Products");
            builder.EntitySet<Application>("Applications").EntityType.HasKey(a => a.Id);
            config.MapODataServiceRoute("ODataRoute", null, builder.GetEdmModel());
        }
    }
}
