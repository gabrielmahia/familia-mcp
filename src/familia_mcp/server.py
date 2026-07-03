"""FamiliaMCP — Kenya Family Infrastructure (6 tools). All data DEMO.

Thesis Layer 10: Families in Africa function like corporations.
Build for inheritance, wills, trusts, diaspora property, caretaker records.
"""
from __future__ import annotations
from typing import Annotated, Optional
from fastmcp import FastMCP
from pydantic import Field

mcp = FastMCP(
    name="familia-mcp",
    instructions="Kenya family infrastructure via MCP — inheritance, wills, trusts, diaspora property, caretaker records. DEMO data only."
)

@mcp.tool(name="succession_law_guide",
          description="Kenya succession law guide — inheritance rights, intestacy rules, gender equity. DEMO.", annotations={"readOnlyHint": True, "openWorldHint": False})
def succession_law_guide(situation: Optional[str] = Field(None, description="Optional filter for situation. Pass None to return all results.")) -> dict:
    SITUATIONS = {
        "intestate":      "When someone dies without a will in Kenya, the Law of Succession Act 1972 applies. Spouse gets life interest in household goods and matrimonial home. Children share estate equally.",
        "widow_rights":   "A surviving spouse has the right to remain in the matrimonial home for life (or until remarriage). Children cannot evict a surviving spouse.",
        "polygamous":     "In polygamous marriages, each house (wife + her children) inherits separately from their portion of the estate.",
        "customary":      "Customary law may apply to land held under customary tenure. However, the High Court has increasingly applied statutory succession equally to men and women.",
        "daughter_rights":"Daughters have equal inheritance rights to sons under the Law of Succession Act. Customary disinheritance is increasingly challenged in courts.",
        "foreign_assets": "Kenyan courts can handle succession of assets in Kenya. Foreign assets (e.g., UK property, US bank accounts) require probate in those jurisdictions separately.",
    }
    if situation:
        s = situation.lower()
        matched = {k: v for k, v in SITUATIONS.items() if k in s or any(w in s for w in k.split("_"))}
        return {"source": "DEMO — Law of Succession Act 1972 (Kenya)", "situation": situation,
                "guidance": matched or SITUATIONS, "disclaimer": "Consult an advocate for specific advice."}
    return {"source": "DEMO — Law of Succession Act 1972", "all_situations": SITUATIONS,
            "legal_aid": "Legal aid: FIDA Kenya (women), Kituo Cha Sheria, LSK Legal Aid Clinic"}

@mcp.tool(name="will_writing_guide",
          description="Guide to writing a legal will in Kenya. DEMO.", annotations={"readOnlyHint": True, "openWorldHint": False})
def will_writing_guide() -> dict:
    return {"source": "DEMO — Law of Succession Act 1972", "requirements": {
        "age": "Must be 18 or older (or married if under 18)",
        "capacity": "Must be of sound mind at time of signing",
        "writing": "Must be in writing (handwritten or typed)",
        "signature": "Must be signed by testator in presence of 2 witnesses",
        "witnesses": "Witnesses must be 18+, present simultaneously, must NOT be beneficiaries",
        "registration": "Not legally required but strongly recommended — register at High Court probate registry",
    }, "what_to_include": [
        "Full legal name and ID number",
        "List of all assets (land titles, bank accounts, businesses, vehicles, household goods)",
        "Named beneficiaries for each asset",
        "Executor (person who implements the will)",
        "Guardian for minor children",
        "Funeral wishes (optional)",
    ], "lawyer_cost": "Will drafting: KES 5,000–20,000 from an advocate",
       "probate_cost": "Probate application: KES 3,000 filing fee at High Court",
       "disclaimer": "Not legal advice. Have your will reviewed by a licensed advocate."}

@mcp.tool(name="diaspora_property_guide",
          description="Guide for Kenya diaspora managing property and estate from abroad. DEMO.", annotations={"readOnlyHint": True, "openWorldHint": False})
def diaspora_property_guide(country: Optional[str] = "USA") -> dict:
    """Return guidance for Kenyan diaspora on managing, inheriting, and protecting property in Kenya."""
    return {"source": "DEMO — Kenya Law Society, Lands Registry", "diaspora_country": country,
            "key_steps": {
                "power_of_attorney": "Appoint a trusted person in Kenya via a Power of Attorney (POA). Must be notarised in your country and apostilled, then registered at Kenya Lands Registry.",
                "title_verification": "Verify land title at Lands Registry (now online via E-Citizens: ecitizen.go.ke). Check for caveats or encumbrances.",
                "property_management": "Engage a licensed property manager or advocate. Agree on rent collection, maintenance, and remittance terms in writing.",
                "inheritance_planning": "Write a will that explicitly covers Kenya property. Name a Kenyan executor who can handle probate locally.",
                "tax": "Land income tax: 30% for non-residents. Pay via iTax (itax.kra.go.ke). CGT on sale: 15% of gain.",
                "remittance": "Use regulated channels (bank transfer, licensed forex) for rent income. Keep records for KRA compliance.",
            }, "key_contacts": {
                "lands_registry": "lands.go.ke | 020-2720550",
                "ecitizen": "ecitizen.go.ke (online title search)",
                "lsk": "Law Society of Kenya: lsk.or.ke (find advocate)",
                "kra": "itax.kra.go.ke (non-resident tax filing)",
            }, "diaspora_investment": "See also: faida-mcp for diaspora investment products (M-Akiba, NSE, REITs)"}

@mcp.tool(name="inheritance_dispute_guide",
          description="Guide to resolving inheritance disputes in Kenya. DEMO.", annotations={"readOnlyHint": True, "openWorldHint": False})
def inheritance_dispute_guide(dispute_type: Optional[str] = Field(None, description="Optional filter for dispute type. Pass None to return all results.")) -> dict:
    PATHS = {
        "family_mediation":   "First step: attempt mediation within family or through a religious leader, community elder, or NCMCC mediator. Free or low cost.",
        "succession_court":   "File at High Court probate and succession registry. Requires filing fee ~KES 3,000. Can petition for letters of administration or contest a will.",
        "caveat":             "Lodge a caveat at High Court probate registry to stop estate distribution pending dispute resolution. Filing fee: KES 500.",
        "land_dispute":       "For land inheritance disputes: Land Disputes Tribunal (county level) is faster than High Court. Free. Decisions can be appealed to ELC.",
        "gender_inequality":  "Women denied inheritance can petition the High Court under Article 27 (equality) and the Law of Succession Act. FIDA Kenya provides legal support: fidakenya.org",
        "foreign_will":       "Foreign wills must be re-sealed in Kenya before taking effect on Kenya assets. Apply to High Court for re-sealing under S.86 Succession Act.",
    }
    if dispute_type:
        d = dispute_type.lower()
        matched = {k: v for k, v in PATHS.items() if k in d or any(w in d for w in k.split("_"))}
        return {"source": "DEMO — High Court, Land Disputes Tribunal", "dispute_type": dispute_type,
                "guidance": matched or PATHS}
    return {"source": "DEMO — Kenya Succession and Land Law", "all_paths": PATHS,
            "free_legal_aid": "FIDA Kenya: fidakenya.org | Kituo Cha Sheria: kituochasheria.or.ke"}

@mcp.tool(name="caretaker_records_guide",
          description="Guide for setting up caretaker arrangements for elderly parents or dependents in Kenya. DEMO.", annotations={"readOnlyHint": True, "openWorldHint": False})
def caretaker_records_guide() -> dict:
    return {"source": "DEMO — Kenya Law, best practice", "why_important":
            "When diaspora families support elderly parents remotely, clear caretaker records prevent disputes, ensure continuity, and protect all parties legally.",
            "recommended_records": {
                "care_agreement": "Written agreement between diaspora family member and caretaker. Include: duties, payment schedule, reporting requirements, termination terms.",
                "medical_authority": "Letter authorising caretaker to make medical decisions in emergencies. Useful for hospital admission.",
                "financial_account": "Dedicated M-PESA or bank account for caretaker expenses. Retain all statements as records.",
                "property_inventory": "Document all household items, title documents, and assets in the home. Photos recommended.",
                "emergency_contacts": "Maintain a written list: nearest family member, doctor, advocate, hospital, nearest police station.",
            }, "payment": {
                "method": "M-PESA or bank transfer with clear description ('care payment MM/YYYY')",
                "tax": "If paying > KES 24,000/month, consider NHIF/NSSF registration for caretaker",
                "minimum_wage": "Domestic worker minimum wage (Nairobi 2025): KES 16,168/month",
            }, "legal_basis": "Employment Act 2007 applies to domestic workers. haki-ya-kazi-mcp for employment rights."}

@mcp.tool(name="trust_structures_kenya",
          description="Guide to trust structures available in Kenya for family wealth protection. DEMO.", annotations={"readOnlyHint": True, "openWorldHint": False})
def trust_structures_kenya(use_case: Optional[str] = Field(None, description="Optional filter for use case. Pass None to return all results.")) -> dict:
    STRUCTURES = {
        "discretionary_trust": {
            "purpose": "Trustee has discretion over distributions. Good for minor children or beneficiaries needing protection.",
            "setup": "Drafted by an advocate. Trustees registered with Capital Markets Authority if investing.",
            "cost": "KES 50,000–150,000 to set up. Annual trustee fee varies.",
        },
        "family_trust": {
            "purpose": "Holds family assets across generations. Good for preventing fragmentation of land.",
            "setup": "Trust deed drafted, trustees appointed (advocate or professional trustee). Land transferred into trust via Lands Registry.",
            "cost": "KES 100,000–300,000+ depending on asset complexity.",
        },
        "unit_trust": {
            "purpose": "Investment trust. Units held by family members. Managed by licensed unit trust manager.",
            "setup": "Invest via existing unit trust (CIC, Old Mutual, Britam). No separate trust deed needed.",
            "cost": "Min investment: KES 1,000–5,000. Annual management fee: 1–2%.",
        },
        "chama_informal": {
            "purpose": "Informal family investment group. Pool resources for land, stocks, business.",
            "setup": "Chama constitution (can be informal), M-PESA paybill or bank account.",
            "cost": "Near zero. jumuia-mcp for SACCO and chama guidance.",
        },
    }
    if use_case:
        u = use_case.lower()
        matched = {k: v for k, v in STRUCTURES.items() if k in u or any(w in u for w in k.split("_"))}
        return {"source": "DEMO — Kenya Trusts Act, CMA", "use_case": use_case,
                "structures": matched or STRUCTURES}
    return {"source": "DEMO — Kenya Trusts Act, Capital Markets Authority", "structures": STRUCTURES,
            "professional_trustee": "Professional trustees: Co-operative Bank Trust, Jubilee Holdings. Cost-effective for larger estates.",
            "disclaimer": "Not legal or financial advice. Consult an advocate or certified financial planner."}
