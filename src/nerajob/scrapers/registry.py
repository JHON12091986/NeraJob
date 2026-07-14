# ============================================
# REGISTRY - CON VALIDACIÓN
# ============================================

from .adzuna import AdzunaScraper
from .remotive import RemotiveScraper
from .himalayas import HimalayasScraper

<<<<<<< HEAD
from nerajob.scrapers.adzuna import AdzunaScraper
=======
<<<<<<< HEAD
>>>>>>> 2750485 (feat: optimize scrapers registry with clean structure)
from nerajob.scrapers.arbeitnow import ArbeitnowScraper
from nerajob.scrapers.ashby import AshbyScraper
from nerajob.scrapers.base import BaseScraper
<<<<<<< HEAD
from nerajob.scrapers.findwork import FindworkScraper
from nerajob.scrapers.jobicy import JobicyScraper
from nerajob.scrapers.jooble import JoobleScraper
=======
<<<<<<< HEAD
from nerajob.scrapers.jobicy import JobicyScraper
=======
from nerajob.scrapers.himalayas import HimalayasScraper  # <-- NUEVO IMPORT
>>>>>>> d9ce0b7 (feat: register Himalayas scraper in registry #5)
>>>>>>> 6de292b (feat: register Himalayas scraper in registry #5)
from nerajob.scrapers.lever import LeverScraper
from nerajob.scrapers.remoteok import RemoteOKScraper
from nerajob.scrapers.remotive import RemotiveScraper
from nerajob.scrapers.sample import SampleScraper
from nerajob.scrapers.smartrecruiters import SmartRecruitersScraper
from nerajob.scrapers.themuse import TheMuseScraper
from nerajob.scrapers.weworkremotely import WeWorkRemotelyScraper
=======
AVAILABLE_SCRAPERS = {
    "adzuna": AdzunaScraper,
    "remotive": RemotiveScraper,
    "himalayas": HimalayasScraper,
}
>>>>>>> c96d534 (feat: optimize scrapers registry with clean structure)

def register_scraper(name, scraper_class):
    """Registra un nuevo scraper en el registro."""
    AVAILABLE_SCRAPERS[name] = scraper_class

def get_scraper(name):
    """Obtiene un scraper por su nombre."""
    return AVAILABLE_SCRAPERS.get(name)

<<<<<<< HEAD
    Lever / Ashby board IDs (optional):
      NERAJOB_LEVER_BOARD   e.g. company slug for api.lever.co
      NERAJOB_ASHBY_BOARD   e.g. board id for api.ashbyhq.com
    Without env, those adapters use offline sample postings (tests/demos).

    Remotive: live public API; set NERAJOB_REMOTIVE_OFFLINE=1 to force offline samples.
    Arbeitnow: live public API; set NERAJOB_ARBEITNOW_OFFLINE=1 for offline samples.
    Jobicy: live public API; set NERAJOB_JOBICY_OFFLINE=1 for offline samples.
    We Work Remotely: RSS feed; set NERAJOB_WWR_OFFLINE=1 for offline samples.
    Smart Recruiters: set NERAJOB_SMARTRECRUITERS_COMPANIES to comma-separated company IDs.
    Findwork: live public API; set NERAJOB_FINDWORK_API_TOKEN env var to use live mode.
              Without token, returns deterministic offline fixtures.
              Set NERAJOB_FINDWORK_OFFLINE=1 to force offline even with token.
    Adzuna: live public API; set ADZUNA_APP_ID + ADZUNA_APP_KEY env vars.
            Without credentials, returns deterministic offline fixtures.
            Set NERAJOB_ADZUNA_OFFLINE=1 to force offline even with credentials.
    """
    scrapers: list[BaseScraper] = [
        SampleScraper(),
        RemoteOKScraper(),
        RemotiveScraper(),
        ArbeitnowScraper(),
        JobicyScraper(),
        JoobleScraper(),
        TheMuseScraper(),
        WeWorkRemotelyScraper(),
        LeverScraper(board_name=os.getenv("NERAJOB_LEVER_BOARD") or None),
        AshbyScraper(board_id=os.getenv("NERAJOB_ASHBY_BOARD") or None),
<<<<<<< HEAD
        SmartRecruitersScraper(),
<<<<<<< HEAD
        FindworkScraper(),
        AdzunaScraper(),
=======
=======
        HimalayasScraper(),  # <-- NUEVO SCRAPER AÑADIDO
>>>>>>> d9ce0b7 (feat: register Himalayas scraper in registry #5)
>>>>>>> 6de292b (feat: register Himalayas scraper in registry #5)
    ]
    return {s.name: s for s in scrapers}


def get_scraper(name: str) -> BaseScraper:
    scrapers = available_scrapers()
    if name not in scrapers:
        known = ", ".join(sorted(scrapers))
        raise KeyError(f"Unknown scraper {name!r}. Known: {known}")
    return scrapers[name]
=======
def list_scrapers():
    """Lista todos los scrapers disponibles."""
    return list(AVAILABLE_SCRAPERS.keys())
>>>>>>> c96d534 (feat: optimize scrapers registry with clean structure)
