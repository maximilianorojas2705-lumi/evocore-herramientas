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

def clasificar_tipo(titulo, snippet):
    """Clasifica la oportunidad por tipo basado en keywords"""
    texto = (titulo + " " + snippet).lower()
    if any(k in texto for k in ["grant", "funding", "subsidy", "bursary"]):
        return "grant"
    elif any(k in texto for k in ["bug bounty", "vulnerability", "security", "hack"]):
        return "bounty"
    elif any(k in texto for k in ["freelance", "job", "hire", "contract", "gig"]):
        return "freelance"
    elif any(k in texto for k in ["sponsor", "patreon", "donate", "tip"]):
        return "sponsor"
    elif any(k in texto for k in ["airdrop", "token", "crypto", "web3"]):
        return "airdrop"
    else:
        return "otro"

def sugerir_accion(tipo):
    """Sugiere el próximo paso según el tipo de oportunidad"""
    acciones = {
        "grant": "📝 Preparar propuesta técnica y enviar aplicación",
        "bounty": "🔍 Analizar plataforma de bug bounty y crear cuenta",
        "freelance": "💼 Actualizar perfil y enviar propuestas personalizadas",
        "sponsor": "🤝 Contactar al sponsor con propuesta de valor",
        "airdrop": "🪙 Verificar elegibilidad y completar tareas requeridas",
        "otro": "🔎 Investigar más detalles antes de actuar"
    }
    return acciones.get(tipo, acciones["otro"])

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
        
        # Clasificación y acción
        tipo = clasificar_tipo(opp.get("titulo", ""), opp.get("snippet", ""))
        opp["tipo"] = tipo
        opp["accion"] = sugerir_accion(tipo)
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
        reporte += f"   Tipo: {opp['tipo'].upper()}{NL}"
        reporte += f"   URL: {opp['url']}{NL}"
        reporte += f"   Score: {opp['score']}%{NL}"
        reporte += f"   Acción: {opp['accion']}{NL}"
        reporte += f"   {opp['snippet'][:100]}...{NL}{NL}"
    
    return reporte

if __name__ == "__main__":
    print(generar_reporte())
