# Kit de Lanzamiento para EvoCore

## 1. Perfil y Propuestas de Servicio para Workana (español)

**Perfil:**
Soy desarrollador full‑stack especializado en automatización con IA, creación de agentes conversacionales y pipelines de datos. Tengo experiencia en proyectos open‑source (Earnfi, Nexus‑Backend) y en la generación de ingresos mediante bots y scrapers.

**Propuestas de Servicio:**
1. **Automatización de procesos de negocio con IA** – Diseño e implementación de agentes que extraen datos, generan reportes y ejecutan acciones en plataformas SaaS. Precio: $30/h.
2. **Desarrollo de scrapers y pipelines de datos** – Recolección, limpieza y análisis de datos de fuentes web y APIs, con entrega de dashboards interactivos. Precio: $25/h.
3. **Integración de herramientas de IA en productos existentes** – Añadir funcionalidades de generación de texto, clasificación y detección de anomalías a apps Python/Node. Precio: $35/h.

---  

## 2. Página de venta en Gumroad (inglés y español) – "AI Opportunity Radar"

**Título:** AI Opportunity Radar – Find Grants, Bounties, Freelance Gigs & Airdrops  

**Precio sugerido:** $19.99 (one‑time) / $4.99/month subscription for updates  

**Descripción (EN):**
A curated toolkit that scans the web daily for high‑value AI‑related opportunities: grants, bug bounties, freelance projects, and crypto airdrops. Includes a Python library, ready‑to‑run scripts, and a Telegram bot that delivers the top 5 opportunities every morning.

**Descripción (ES):**
Un kit curado que escanea la web a diario en busca de oportunidades de alto valor relacionadas con IA: grants, bug bounties, proyectos freelance y airdrops de cripto. Incluye una librería Python, scripts listos para ejecutar y un bot de Telegram que entrega las 5 mejores oportunidades cada mañana.

**Incluye:**
- `tools/oportunidades.py` – búsqueda y filtrado avanzado.
- `tools/cripto_radar.py` – monitor de precios y arbitrajes.
- Configuración de autotareas para recibir reportes vía Telegram.
- Guía de instalación y uso paso a paso.

---  

## 3. Resumen de proyecto EvoCore (formato hackathon)

**Problema:**
Los freelancers y startups pierden tiempo valioso buscando oportunidades de financiación, bug bounties y gigs, y no pueden automatizar la detección ni el seguimiento.

**Solución:**
EvoCore es un agente autónomo que, mediante tareas programadas, busca en fuentes abiertas (Tavily, APIs públicas) y entrega reportes estructurados por Telegram. Permite clasificación por tipo, puntuación y acciones sugeridas.

**Arquitectura:**
- **Frontend:** Bot de Telegram (Python‑telegram‑bot).
- **Backend:** Scripts Python en la nube, ejecutados con `ejecutar_python`.
- **Data Layer:** Búsquedas con Tavily, procesamiento con `tools/oportunidades.py` y `tools/cripto_radar.py`.
- **Persistencia:** Memoria en GitHub (`memoria.json`), historial de mejoras y recordatorios.

**Demo:**
1. El bot envía a las 08:00 y 20:00 el reporte de oportunidades.
2. El usuario recibe enlaces directos a grants, bounties y gigs con fechas límite.
3. Con un solo comando (`/oportunidades`) se muestra el último radar.

**Repositorios:**
- https://github.com/maximilianorojas2705-lumi/evocore-memoria
- https://github.com/maximilianorojas2705-lumi/evocore-herramientas
- https://github.com/maximilianorojas2705-lumi/Earnfi
- https://github.com/maximilianorojas2705-lumi/nexus-backend
