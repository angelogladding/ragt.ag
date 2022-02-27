"""Personal website for Angelo Gladding."""

import web
from understory import code

app = web.application(__name__, db=True, mounts=[code.app])


@app.control("")
class Home:
    """Profile and primary feed."""

    def get(self):
        """Render a profile summary and a reverse chronological feed of public posts."""
        return app.view.index()
