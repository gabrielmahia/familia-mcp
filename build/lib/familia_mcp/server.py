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
          description="Explain how inheritance works in Kenya under the Law of Succession Act 1972: what happens when someone dies with or without a will, who inherits, and the court process. Use when a family asks what to do after a death. Keywords in situation select entries; if none match, ALL situations are returned; with no argument it returns every situation and legal-aid contacts. Returns the source label, the situation, the guidance and a disclaimer. A summary labelled DEMO and not legal advice: consult an advocate, FIDA Kenya or Kituo Cha Sheria. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def succession_law_guide(situation: str | None = Field(None, description="Optional filter for situation. Pass None to return all results.")) -> dict:
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
          description="Requirements and steps for making a valid will in Kenya: age, capacity, witnesses, what to include, indicative advocate and probate costs. Use when someone asks how to write a will. Takes no arguments. Returns the source label, requirements, contents to include, indicative costs and a disclaimer. Fees are indicative and labelled DEMO: have a licensed advocate review the will. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
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
          description="Steps for a Kenyan abroad to manage family property at home: power of attorney, land searches, a trusted representative, tax filing and records. Use when a diaspora family asks how to look after land or a house remotely. country is only echoed back; the same steps are returned for everyone. Returns the source label, the echoed country, the key steps, contacts such as the Lands registry and the Law Society of Kenya, and a pointer to faida-mcp. A static guide labelled DEMO and not legal advice: use a licensed advocate. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def diaspora_property_guide(country: Annotated[str | None, Field(description="Country of residence such as USA; only echoed back (default USA).")] = "USA") -> dict:
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
          description="Routes to resolve a family inheritance dispute in Kenya: mediation first, then the court or tribunal, with free legal-aid options. Use when relatives disagree about an estate. Keywords in dispute_type select entries; if none match, ALL paths are returned; with no argument it lists all paths and legal-aid contacts. Returns the source label, the dispute type and the guidance. A static summary labelled DEMO and not legal advice: consult an advocate. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def inheritance_dispute_guide(dispute_type: str | None = Field(None, description="Optional filter for dispute type. Pass None to return all results.")) -> dict:
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
          description="How to keep clear records when diaspora family members pay for the care of elderly parents remotely: what to write down, how to pay and the employment rules that may apply to a caretaker. Use when a family wants to avoid disputes over care payments. Takes no arguments. Returns the source label, why records matter, what to record, payment practice, an indicative wage and tax note and the legal basis. The wage and contribution figures are indicative and unverified (labelled DEMO): check current minimum wages and SHA and NSSF rules. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
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
                "tax": "If paying > KES 24,000/month, consider SHA (formerly NHIF) and NSSF registration for caretaker",
                "minimum_wage": "Domestic worker minimum wage from 1 May 2026 (Regulation of Wages (General) (Amendment) Order, 2026): KES 18,047.40 a month in Nairobi, Mombasa, Kisumu, Nakuru and Eldoret, KES 9,268 elsewhere. Reported by FKE and the press: verify with the Ministry of Labour.",
            }, "legal_basis": "Employment Act 2007 applies to domestic workers. haki-ya-kazi-mcp for employment rights."}

@mcp.tool(name="trust_structures_kenya",
          description="Compare trust structures available in Kenya (such as discretionary and family trusts) with purpose and when each fits, plus the role of professional trustees. Use when someone asks how to hold assets for family. Keywords in use_case select entries; if none match, ALL structures are returned. Returns the source label, the structures, professional-trustee notes and a disclaimer. A static summary labelled DEMO and not legal or financial advice: consult an advocate or planner. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def trust_structures_kenya(use_case: str | None = Field(None, description="Optional filter for use case. Pass None to return all results.")) -> dict:
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

def main() -> None:
    """Console entry point."""
    mcp.run()
