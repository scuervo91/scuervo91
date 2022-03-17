from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=100)

tree =  Tree("Santiago Cuervo", guide_style="bold green")
res_tree = tree.add(":oil_drum: Integral Reservoir Engineer")
dev_tree = tree.add(":computer: Developer")
python_tree = dev_tree.add(":snake: Python")
python_tree.add(":star2:[link=https://github.com/scuervo91/fieldspy]Fieldspy")
python_tree.add(":star2:[link=https://github.com/scuervo91/dcapy]Dcapy")
python_tree.add(":star2:[link=https://github.com/scuervo91/wellschematicspy]WellschematicsPy")
python_tree.add(":star2:[link=https://github.com/scuervo91/volumetricspy]Volumetricspy")
python_tree.add(":star2:[link=https://github.com/scuervo91/krpy]Krpy")
python_tree.add(":star2:[link=https://github.com/scuervo91/pvtpy]pvtpy")
python_tree.add(":fire:[link=https://github.com/scuervo91/resimpy]resimpy (On Dev)")
python_tree.add(":fire:[link=https://github.com/scuervo91/decisionpy]decisionpy (On Dev)")
python_tree.add(":fire:[link=https://github.com/scuervo91/flowpy]flowpy (On Dev)")
dev_tree.add(":whale2: Docker/Compose/Swarm")
dev_tree.add(":file_cabinet: Databases")
dev_tree.add(":cloud: WebApps/APIs")
res_tree.add(":tokyo_tower: Simulation")
res_tree.add(":tokyo_tower: Forecasting")
res_tree.add(":tokyo_tower: Reserves Portfolio")
res_tree.add(":tokyo_tower: Well Testing")
res_tree.add(":tokyo_tower: Proyects Evaluation")

about = """\
I'm an Integral Reservoir Engineer for Oil&Gas Industry. I've been collecting some of the Reservoir Engineering 
workflows on different Python Packages. These workflows aim to cover most of the life-time phases of a reservoir:

* Well Logs Viewer and Interpretation
* Dca Forecast
* Volumetric Analysis
* Material Balance
* Pvt
* Simulation

All workflows have been implemented on the [link=https://github.com/scuervo91/reservoirpy]Reservoirpy repository. However,
these workflows are goint to have their own repository/package for better maintenance and documentation. 

So far, next are the packages already published on pypi to be used.

* [link=https://github.com/scuervo91/dcapy]Dcapy - Decline Curve Analysis
* [link=https://github.com/scuervo91/wellschematicspy]WellschematicsPy" - Simple Well Schematics viewer on Matplotlib
"""

panel = Panel.fit(
    about, box=box.DOUBLE, border_style="blue", title="[b]About", width=60
)


console.print(Columns([panel, tree]))


CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)



