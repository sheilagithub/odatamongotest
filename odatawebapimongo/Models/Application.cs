using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace odatawebapimongo.Models
{
    public class Application
    {
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        public string Id { get; set; }


        [BsonElement("FRN")]
        public string Frn { get; set; }

        [BsonElement("_date")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string RecordDate { get; set; }


        [BsonElement("471 Application Number")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string ApplicationNumber471 { get; set; }

        [BsonElement("471 Form Status")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string FormStatus471 { get; set; }

        [BsonElement("470 Application Number")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string ApplicationNumber470 { get; set; }

        [BsonElement("470 Form Status")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string FormStatus470 { get; set; }

        [BsonElement("Applicant Name")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string ApplicantName { get; set; }

        [BsonElement("BEN")]
        [BsonIgnoreIfNull]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string Ben { get; set; }

        [BsonElement("Application Type")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string ApplicationType { get; set; }

        [BsonElement("Applicant Street Address1")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string ApplicantStreetAddress1 { get; set; }

        [BsonElement("Applicant Street Address2")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string ApplicantStreetAddress2 { get; set; }

        [BsonElement("Applicant City")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string ApplicantCity { get; set; }

        [BsonElement("Applicant State")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string ApplicantState { get; set; }

        [BsonElement("Applicant Zip Code")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string ApplicantZipCode { get; set; }

        [BsonElement("SPIN")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string Spin { get; set; }

        [BsonElement("Service Provider Name")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string ServiceProviderName { get; set; }

        [BsonElement("Commitment Status")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string CommitmentStatus { get; set; }

        [BsonElement("FCDL Comment")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string FcdlComment { get; set; }


        [BsonElement("486 SSD")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string Ssd486 { get; set; }

        [BsonElement("Funding Year")]
        [BsonIgnoreIfNull]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string FundingYear { get; set; }

        [BsonElement("FCDL Date")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string FcdlDate { get; set; }

        [BsonElement("Contract Exp Date")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string ContractExpDate { get; set; }

        [BsonElement("Last Date to Invoice")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string LastDatetoInvoice { get; set; }

        [BsonElement("Orig FRN Service Type")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string OrigFrnServiceType { get; set; }

        [BsonElement("Orig R Monthly Cost")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string OrigRMonthlyCost { get; set; }

        [BsonElement("Orig R Ineligible Cost")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string OrigRIneligibleCost { get; set; }

        [BsonElement("Orig R Eligible Cost")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string OrigREligibleCost { get; set; }

        [BsonElement("Orig R Months of Service")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string OrigRMonthsofService { get; set; }

        [BsonElement("Orig R Annual Cost")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string OrigRAnnualCost { get; set; }

        [BsonElement("Orig NR Cost")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string OrigNrCost { get; set; }

        [BsonElement("Orig NR Ineligible Cost")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string OrigNrIneligibleCost { get; set; }

        [BsonElement("Orig NR Eligible Cost")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string OrigNrEligibleCost { get; set; }

        [BsonElement("Orig Total Cost")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string OrigTotalCost { get; set; }
        [BsonElement("Orig Discount")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string OrigDiscount { get; set; }
        [BsonElement("Orig Commitment Request")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string OrigCommitmentRequest { get; set; }
        [BsonElement("Cmtd FRN Service Type")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string CmtdFrnServiceType { get; set; }
        [BsonElement("Committed Amount")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string CommittedAmount { get; set; }
        [BsonElement("Cmtd R Monthly Cost")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string CmtdRMonthlyCost { get; set; }
        [BsonElement("Cmtd R Ineligible Cost")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string CmtdRIneligibleCost { get; set; }
        [BsonElement("Cmtd R Eligible Cost")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string CmtdREligibleCost { get; set; }
        [BsonElement("Cmtd R Months of Service")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string CmtdRMonthsofService { get; set; }
        [BsonElement("Cmtd R Annual Cost")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string CmtdRAnnualCost { get; set; }
        [BsonElement("Cmtd NR Cost")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string CmtdNrCost { get; set; }
        [BsonElement("Cmtd NR Ineligible Cost")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string CmtdNrIneligibleCost { get; set; }
        [BsonElement("Cmtd NR Eligible Cost")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string CmtdNrEligibleCost { get; set; }
        [BsonElement("Cmtd Total Cost")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string CmtdTotalCost { get; set; }
        [BsonElement("Cmtd Discount")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string CmtdDiscount { get; set; }
        [BsonElement("Cmtd Commitment Request")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string CmtdCommitmentRequest { get; set; }
        [BsonElement("Orig 471 SSD")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string Orig471Ssd { get; set; }
        [BsonElement("Cmtd 471 SSD")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string Cmtd471Ssd { get; set; }
        [BsonElement("Invoicing Mode")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string InvoicingMode { get; set; }
        [BsonElement("Site Identifier")]
        [BsonIgnoreIfNull]
        public object SiteIdentifier { get; set; }
        [BsonElement("Total Authorized Disbursement")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string TotalAuthorizedDisbursement { get; set; }
        [BsonElement("Wave Number")]
        public object WaveNumber { get; set; }
        [BsonElement("Appeal Wave Number")]
        [BsonSerializer(typeof(CustomStringSerializer))]
        public string AppealWaveNumber { get; set; }

        [BsonExtraElements]
        public BsonDocument CatchAll { get; set; }

    }
}