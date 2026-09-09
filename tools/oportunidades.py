import requests, os

def buscar_oportunidades():
    """Busca oportunidades de monetización con $0 inversión"""
    queries = [
        "AI open source grants 2026",
        "bug bounty high paying",
        "freelance AI automation",
        "crypto airdrops confirmed",
        "GitHub sponsors monetization"
    ]
    
    oportunidades = []
    for q in queries:
        r = requests.post(
            "https://api.tavily.com/search",
            json={"query": q, "max_results": 3},
            headers={"Authorization": "Bearer " + os.environ["TAVILY_KEY"]},
            timeout=20
        )
        if r.ok:
            for item in r.json().get("results", []):
                oportunidades.append({
                    "titulo": item.get("title", ""),
                    "url": item.get("url", ""),
                    "snippet": item.get("content", "")[:200]
                })
    
    return oportunidades

def rankear_oportunidades(oportunidades):
    """Rankea por probabilidad de éxito basado en skills Python/AI"""
    keywords_alta = ["open source", "grant", "python", "automation", "AI"]
    rankeadas = []
    
    for opp in oportunidades:
        score = 0
        texto = (opp.get("titulo", "") + " " + opp.get("snippet", "")).lower()
        
        for kw in keywords_alta:
            if kw in texto:
                score += 20
        
        if opp.get("url"):
            score += 10
        
        opp["score"] = score
        rankeadas.append(opp)
    
    return sorted(rankeadas, key=lambda x: x["score"], reverse=True)

def generar_reporte():
    """Genera reporte de oportunidades accionables"""
    opps = buscar_oportunidades()
    rankeadas = rankear_oportunidades(opps)
    
    NL = chr(10)
    reporte = f"🎯 TOP 5 OPORTUNIDADES $0 INVERSIÓN:{NL}{NL}"
    
    for i, opp in enumerate(rankeadas[:5], 1):
        reporte += f"{i}. {opp['titulo']}{NL}"
        reporte += f"   URL: {opp['url']}{NL}"
        reporte += f"   Score: {opp['score']}%{NL}"
        reporte += f"   {opp['snippet'][:100]}...{NL}{NL}"
    
    return reporte

if __name__ == "__main__":
    print(generar_reporte())
