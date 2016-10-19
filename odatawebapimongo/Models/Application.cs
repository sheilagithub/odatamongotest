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

        //[BsonElement("471 Application Number")]
        //public int ApplicationNumber471 { get; set; }
        //[BsonElement("471 Form Status")]
        //public string FormStatus471 { get; set; }
        //[BsonElement("FRN")]
        //public int Frn { get; set; }
        //[BsonElement("470 Application Number")]
        //public long ApplicationNumber470 { get; set; }
        //[BsonElement("470 Form Status")]
        //public string FormStatus470 { get; set; }
        //[BsonElement("Applicant Name")]
        //public string ApplicantName { get; set; }
        //[BsonElement("BEN")]
        //[BsonIgnoreIfNull]
        //public int Ben { get; set; }
        //[BsonElement("Application Type")]
        //public string ApplicationType { get; set; }
        //[BsonElement("Applicant Street Address1")]
        //public string ApplicantStreetAddress1 { get; set; }
        //[BsonElement("Applicant Street Address2")]
        //public string ApplicantStreetAddress2 { get; set; }
        //[BsonElement("Applicant City")]
        //public string ApplicantCity { get; set; }
        //[BsonElement("Applicant State")]
        //public string ApplicantState { get; set; }
        //[BsonElement("Applicant Zip Code")]
        //public int ApplicantZipCode { get; set; }
        //[BsonElement("SPIN")]
        //public int Spin { get; set; }
        //[BsonElement("Service Provider Name")]
        //public string ServiceProviderName { get; set; }
        //[BsonElement("Commitment Status")]
        //public string CommitmentStatus { get; set; }
        //[BsonElement("FCDL Comment")]
        //public string FcdlComment { get; set; }

        //[BsonElement("486 SSD")]
        //public string Ssd486 { get; set; }

        //[BsonElement("Funding Year")]
        //[BsonIgnoreIfNull]
        //public int FundingYear { get; set; }
        //[BsonElement("FCDL Date")]
        //public string FcdlDate { get; set; }
        //[BsonElement("Contract Exp Date")]
        //public string ContractExpDate { get; set; }
        //[BsonElement("Last Date to Invoice")]
        //public string LastDatetoInvoice { get; set; }
        //[BsonElement("Orig FRN Service Type")]
        //public string OrigFrnServiceType { get; set; }
        //[BsonElement("Orig R Monthly Cost")]
        //public string OrigRMonthlyCost { get; set; }
        //[BsonElement("Orig R Ineligible Cost")]
        //public string OrigRIneligibleCost { get; set; }
        //[BsonElement("Orig R Eligible Cost")]
        //public string OrigREligibleCost { get; set; }
        //[BsonElement("Orig R Months of Service")]
        //public int OrigRMonthsofService { get; set; }
        //[BsonElement("Orig R Annual Cost")]
        //public string OrigRAnnualCost { get; set; }
        //[BsonElement("Orig NR Cost")]
        //public string OrigNrCost { get; set; }
        //[BsonElement("Orig NR Ineligible Cost")]
        //public string OrigNrIneligibleCost { get; set; }
        //[BsonElement("Orig NR Eligible Cost")]
        //public string OrigNrEligibleCost { get; set; }
        //[BsonElement("Orig Total Cost")]
        //public string OrigTotalCost { get; set; }
        //[BsonElement("Orig Discount")]
        //public double OrigDiscount { get; set; }
        //[BsonElement("Orig Commitment Request")]
        //public string OrigCommitmentRequest { get; set; }
        //[BsonElement("Cmtd FRN Service Type")]
        //public string CmtdFrnServiceType { get; set; }
        //[BsonElement("Committed Amount")]
        //public string CommittedAmount { get; set; }
        //[BsonElement("Cmtd R Monthly Cost")]
        //public string CmtdRMonthlyCost { get; set; }
        //[BsonElement("Cmtd R Ineligible Cost")]
        //public string CmtdRIneligibleCost { get; set; }
        //[BsonElement("Cmtd R Eligible Cost")]
        //public string CmtdREligibleCost { get; set; }
        //[BsonElement("Cmtd R Months of Service")]
        //public int CmtdRMonthsofService { get; set; }
        //[BsonElement("Cmtd R Annual Cost")]
        //public string CmtdRAnnualCost { get; set; }
        //[BsonElement("Cmtd NR Cost")]
        //public string CmtdNrCost { get; set; }
        //[BsonElement("Cmtd NR Ineligible Cost")]
        //public string CmtdNrIneligibleCost { get; set; }
        //[BsonElement("Cmtd NR Eligible Cost")]
        //public string CmtdNrEligibleCost { get; set; }
        //[BsonElement("Cmtd Total Cost")]
        //public string CmtdTotalCost { get; set; }
        //[BsonElement("Cmtd Discount")]
        //public double CmtdDiscount { get; set; }
        //[BsonElement("Cmtd Commitment Request")]
        //public string CmtdCommitmentRequest { get; set; }
        //[BsonElement("Orig 471 SSD")]
        //public string Orig471Ssd { get; set; }
        //[BsonElement("Cmtd 471 SSD")]
        //public string Cmtd471Ssd { get; set; }
        //[BsonElement("Invoicing Mode")]
        //public string InvoicingMode { get; set; }
        //[BsonElement("Site Identifier")]
        //[BsonIgnoreIfNull]
        //public object SiteIdentifier { get; set; }
        //[BsonElement("Total Authorized Disbursement")]
        //public string TotalAuthorizedDisbursement { get; set; }
        //[BsonElement("Wave Number")]
        //public object WaveNumber { get; set; }
        //[BsonElement("Appeal Wave Number")]
        //public string AppealWaveNumber { get; set; }

        [BsonExtraElements]
        public BsonDocument CatchAll { get; set; }

    }
}