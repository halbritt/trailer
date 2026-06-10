#!/usr/bin/env python3
"""Generate a Juplaya trailer power diagram using the reference diagram schema."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


OUT = Path("docs/reference/juplaya-power-diagram.json")


def prop(node_id: str, key: str, name: str, value: str, visible: bool = True) -> dict[str, Any]:
    return {
        "id": f"{node_id}-{key}",
        "name": name,
        "value": value,
        "visible": visible,
        "isDefault": True,
    }


def port(node_id: str, suffix: str, side: str, kind: str, index: int) -> dict[str, Any]:
    return {
        "id": f"{node_id}-{suffix}",
        "side": side,
        "kind": kind,
        "index": index,
    }


def node(
    nodes: list[dict[str, Any]],
    node_id: str,
    node_type: str,
    x: int,
    y: int,
    ports: list[dict[str, Any]],
    data: dict[str, Any],
) -> str:
    nodes.append({"id": node_id, "type": node_type, "x": x, "y": y, "ports": ports, "data": data})
    return node_id


def rect(nodes: list[dict[str, Any]], node_id: str, x: int, y: int, width: int, height: int, color: str) -> None:
    node(
        nodes,
        node_id,
        "rect",
        x,
        y,
        [],
        {
            "label": "",
            "brand": "generic",
            "category": "general",
            "componentId": "rect",
            "width": width,
            "height": height,
            "zIndex": -1,
            "fillColor": color,
            "locked": True,
        },
    )


def text(nodes: list[dict[str, Any]], node_id: str, label: str, x: int, y: int, size: int = 42) -> None:
    node(
        nodes,
        node_id,
        "text",
        x,
        y,
        [],
        {
            "label": label,
            "brand": "generic",
            "category": "general",
            "componentId": "text",
            "width": 420,
            "height": 110,
            "fontSize": size,
            "fontColor": "#000000",
            "textAlign": "center",
        },
    )


def lead_label(nodes: list[dict[str, Any]], node_id: str, label: str, x: int, y: int) -> None:
    node(
        nodes,
        node_id,
        "text",
        x,
        y,
        [],
        {
            "label": label,
            "brand": "generic",
            "category": "general",
            "componentId": "text",
            "width": 250,
            "height": 70,
            "fontSize": 22,
            "fontColor": "#475569",
            "textAlign": "center",
        },
    )


def solar_panel(nodes: list[dict[str, Any]], node_id: str, label: str, x: int, y: int, watts: int = 455) -> None:
    node(
        nodes,
        node_id,
        "solarPanel",
        x,
        y,
        [
            port(node_id, "pv-plus", "bottom", "PV+", 0),
            port(node_id, "pv-minus", "bottom", "PV-", 1),
        ],
        {
            "label": label,
            "brand": "generic",
            "category": "solar",
            "componentId": "monocrystalline-panel",
            "rated-power": watts,
            "voc": 49.9,
            "seriesAllowed": True,
            "width": 175,
            "height": 250,
            "properties": [
                prop(node_id, "rated-power", "Rated Power", f"{watts} W"),
                prop(node_id, "voc", "Open-circuit Voltage (Voc)", "49.9 V", False),
                prop(node_id, "impp", "MPP Current", "10.83 A"),
                prop(node_id, "isc", "Short-circuit Current", "11.39 A", False),
            ],
            "labelFontSizePx": 15,
            "metadataFontSize": 13,
        },
    )


def mppt(nodes: list[dict[str, Any]], node_id: str, label: str, x: int, y: int, amps: int, max_voc: int) -> None:
    node(
        nodes,
        node_id,
        "solar",
        x,
        y,
        [
            port(node_id, "dc-minus-a", "bottom", "DC-", 2),
            port(node_id, "dc-plus-a", "bottom", "DC+", 3),
            port(node_id, "dc-minus-b", "bottom", "DC-", 4),
            port(node_id, "dc-plus-b", "bottom", "DC+", 5),
            port(node_id, "pv-plus", "top", "PV+", 0),
            port(node_id, "pv-minus", "top", "PV-", 1),
            port(node_id, "ground", "left", "GND", 0),
        ],
        {
            "label": label,
            "brand": "generic",
            "category": "solar",
            "componentId": "mppt-controller",
            "ampRating": amps,
            "maxInputVoltage": max_voc,
            "outputVoltage": 48,
            "width": 360,
            "height": 244,
            "properties": [
                prop(node_id, "system-voltage", "System Voltage", "48 V", False),
                prop(node_id, "rated-charge-current", "Rated Charge Current", f"{amps} A"),
                prop(node_id, "max-pv-voc", "Max PV Open-circuit Voltage (Voc)", f"{max_voc} V", False),
            ],
            "labelFontSizePx": 21,
            "metadataFontSize": 18,
        },
    )


def mcb_double(nodes: list[dict[str, Any]], node_id: str, label: str, x: int, y: int, amps: int, volts: int) -> None:
    node(
        nodes,
        node_id,
        "mcb-double",
        x,
        y,
        [
            port(node_id, "pv-plus-in", "top", "PV+", 0),
            port(node_id, "pv-minus-in", "top", "PV-", 1),
            port(node_id, "pv-plus-out", "bottom", "PV+", 0),
            port(node_id, "pv-minus-out", "bottom", "PV-", 1),
        ],
        {
            "label": label,
            "brand": "generic",
            "category": "fuses",
            "componentId": "dc-mcb-double",
            "poles": "Double",
            "rated-current": amps,
            "trip-curve": "B",
            "rated-voltage": volts,
            "width": 70,
            "height": 105,
            "properties": [
                prop(node_id, "poles", "Poles", "Double"),
                prop(node_id, "rated-current", "Rated Current", f"{amps} A"),
                prop(node_id, "rated-voltage", "Rated Voltage", f"{volts} V", False),
            ],
        },
    )


def breaker(nodes: list[dict[str, Any]], node_id: str, label: str, x: int, y: int, amps: int, volts: int = 80) -> None:
    node(
        nodes,
        node_id,
        "mcb",
        x,
        y,
        [
            port(node_id, "dc-plus-in", "left", "DC+", 0),
            port(node_id, "dc-plus-out", "right", "DC+", 0),
        ],
        {
            "label": label,
            "brand": "generic",
            "category": "fuses",
            "componentId": "dc-inline-breaker",
            "rated-current": amps,
            "rated-voltage": volts,
            "poles": "Single",
            "width": 90,
            "height": 80,
            "properties": [
                prop(node_id, "rated-current", "Rated Current", f"{amps} A"),
                prop(node_id, "rated-voltage", "Rated Voltage", f"{volts} V", False),
                prop(node_id, "poles", "Poles", "Single", False),
            ],
        },
    )


def busbar(nodes: list[dict[str, Any]], node_id: str, label: str, kind: str, x: int, y: int) -> None:
    ports = [
        port(node_id, f"top-{i}", "top", kind, i) for i in range(6)
    ] + [
        port(node_id, f"bottom-{i}", "bottom", kind, i) for i in range(6)
    ]
    if kind == "DC-":
        ports.append(port(node_id, "ground", "left", "GND", 0))
    node(
        nodes,
        node_id,
        "busbar",
        x,
        y,
        ports,
        {
            "label": label,
            "brand": "generic",
            "category": "busbars",
            "componentId": "positive-busbar" if kind == "DC+" else "negative-busbar",
            "rated-current": 300,
            "width": 430,
            "height": 120,
            "properties": [prop(node_id, "rated-current", "Rated Current", "300 A", False)],
            "labelFontSizePx": 21,
        },
    )


def battery(nodes: list[dict[str, Any]], node_id: str, x: int, y: int) -> None:
    node(
        nodes,
        node_id,
        "battery",
        x,
        y,
        [
            port(node_id, "dc-minus", "top", "DC-", 0),
            port(node_id, "dc-plus", "top", "DC+", 1),
        ],
        {
            "label": "LiTime 48 V 100 Ah ComFlex",
            "brand": "generic",
            "category": "batteries",
            "componentId": "lithium-battery",
            "system-voltage": 48,
            "capacity": 100,
            "chemistry": "LiFePO4",
            "integrated-bms": "Yes",
            "seriesAllowed": False,
            "width": 390,
            "height": 240,
            "properties": [
                prop(node_id, "system-voltage", "System Voltage", "48 V", False),
                prop(node_id, "capacity", "Capacity", "100 Ah / 5.12 kWh"),
                prop(node_id, "chemistry", "Chemistry", "LiFePO4", False),
                prop(node_id, "continuous-current", "Continuous Current", "100 A charge/discharge"),
            ],
            "labelFontSizePx": 18,
            "metadataFontSize": 15,
        },
    )


def class_t(nodes: list[dict[str, Any]], node_id: str, label: str, x: int, y: int, amps: int) -> None:
    node(
        nodes,
        node_id,
        "fuse",
        x,
        y,
        [
            port(node_id, "dc-plus-in", "bottom", "DC+", 0),
            port(node_id, "dc-plus-out", "top", "DC+", 0),
        ],
        {
            "label": label,
            "brand": "generic",
            "category": "fuses",
            "componentId": "class-t-fuse",
            "rated-current": amps,
            "width": 120,
            "height": 30,
            "properties": [prop(node_id, "rated-current", "Rated Current", f"{amps} A")],
            "rotation": 90,
        },
    )


def shunt(nodes: list[dict[str, Any]], node_id: str, x: int, y: int) -> None:
    node(
        nodes,
        node_id,
        "component",
        x,
        y,
        [
            port(node_id, "dc-minus-in", "left", "DC-", 1),
            port(node_id, "dc-minus-out", "right", "DC-", 1),
            port(node_id, "sig", "top", "SIG", 0),
            port(node_id, "dc-plus-sense", "top", "DC+", 1),
        ],
        {
            "label": "500 A Shunt",
            "brand": "generic",
            "category": "monitoring",
            "componentId": "shunt",
            "width": 210,
            "height": 65,
            "ampRating": 500,
            "rotation": 90,
            "properties": [
                prop(node_id, "shunt-rating", "Shunt Rating", "500 A"),
                prop(node_id, "system-voltage", "System Voltage", "48 V", False),
            ],
        },
    )


def dcdc(
    nodes: list[dict[str, Any]],
    node_id: str,
    label: str,
    x: int,
    y: int,
    in_v: int,
    out_v: int,
    amps: int,
    watts: int,
) -> None:
    node(
        nodes,
        node_id,
        "dcdc",
        x,
        y,
        [
            port(node_id, "out-plus", "bottom", "DC+", 2),
            port(node_id, "out-minus", "bottom", "DC-", 3),
            port(node_id, "ground", "right", "GND", 0),
            port(node_id, "in-plus", "top", "DC+", 0),
            port(node_id, "in-minus", "top", "DC-", 1),
        ],
        {
            "label": label,
            "brand": "generic",
            "category": "dcdc-chargers",
            "componentId": "smart-charger-dcdc",
            "ampRating": amps,
            "inputVoltage": in_v,
            "outputVoltage": out_v,
            "isIsolated": True,
            "hasDPlus": False,
            "width": 360,
            "height": 176,
            "properties": [
                prop(node_id, "input-voltage", "Input Voltage", f"{in_v} V", False),
                prop(node_id, "output-voltage", "Output Voltage", f"{out_v} V", False),
                prop(node_id, "rated-current", "Rated Output Current", f"{amps} A"),
                prop(node_id, "rated-power", "Rated Output Power", f"{watts} W"),
                prop(node_id, "isolation", "Isolation", "Isolated", False),
            ],
            "labelFontSizePx": 20,
            "metadataFontSize": 16,
        },
    )


def fusebox(nodes: list[dict[str, Any]], node_id: str, label: str, x: int, y: int, circuits: int = 12) -> None:
    ports = [
        port(node_id, "input-plus", "top", "DC+", 0),
        port(node_id, "input-minus", "bottom", "DC-", 0),
    ]
    for side in ("left", "right"):
        for i in range(circuits // 2):
            ports.append(port(node_id, f"{side}-plus-{i}", side, "DC+", i * 2))
            ports.append(port(node_id, f"{side}-minus-{i}", side, "DC-", i * 2 + 1))
    node(
        nodes,
        node_id,
        "fusebox",
        x,
        y,
        ports,
        {
            "label": label,
            "brand": "generic",
            "category": "fuses",
            "componentId": "dc-fuse-box",
            "bladeCount": circuits,
            "bladeRatings": [],
            "width": 165,
            "height": 280,
            "fuses": [],
            "labelFontSizePx": 18,
        },
    )


def custom_dc(
    nodes: list[dict[str, Any]],
    node_id: str,
    label: str,
    x: int,
    y: int,
    voltage: str,
    current: str,
    power: str = "",
    width: int = 300,
    height: int = 180,
    extra_ports: list[dict[str, Any]] | None = None,
) -> None:
    ports = [
        port(node_id, "dc-plus", "left", "DC+", 0),
        port(node_id, "dc-minus", "left", "DC-", 1),
    ]
    if extra_ports:
        ports.extend(extra_ports)
    node(
        nodes,
        node_id,
        "custom",
        x,
        y,
        ports,
        {
            "label": label,
            "brand": "generic",
            "category": "general",
            "componentId": "custom-dc",
            "width": width,
            "height": height,
            "properties": [
                prop(node_id, "operating-voltage", "Operating Voltage", voltage, bool(voltage)),
                prop(node_id, "rated-current", "Rated Current", current, bool(current)),
                prop(node_id, "rated-power", "Rated Power", power, bool(power)),
            ],
            "labelFontSizePx": 18,
        },
    )


def ground_point(nodes: list[dict[str, Any]], node_id: str, label: str, x: int, y: int) -> None:
    node(
        nodes,
        node_id,
        "groundPoint",
        x,
        y,
        [
            port(node_id, "chassis-top", "top", "CHASSIS", 0),
            port(node_id, "chassis-right-a", "right", "CHASSIS", 0),
            port(node_id, "chassis-right-b", "right", "CHASSIS", 1),
        ],
        {
            "label": label,
            "brand": "generic",
            "category": "busbars",
            "componentId": "chassis-ground-point",
            "groundType": "DC",
            "width": 130,
            "height": 130,
            "labelFontSizePx": 20,
        },
    )


def wire(
    wires: list[dict[str, Any]],
    wire_id: str,
    source_node: str,
    source_port: str,
    target_node: str,
    target_port: str,
    size: float,
    midpoints: list[tuple[int, int]] | None = None,
    mode: str = "manual",
) -> None:
    wires.append(
        {
            "id": wire_id,
            "sourceNodeId": source_node,
            "sourcePortId": source_port,
            "targetNodeId": target_node,
            "targetPortId": target_port,
            "midpoints": [
                {"id": f"{wire_id}-mid-{i}", "x": x, "y": y}
                for i, (x, y) in enumerate(midpoints or [], start=1)
            ],
            "routingMode": mode,
            "wireSize": size,
            "wireSizeUnit": "mm2",
            "isAutoSized": True,
        }
    )


def build() -> dict[str, Any]:
    nodes: list[dict[str, Any]] = []
    wires: list[dict[str, Any]] = []

    # Section backgrounds and labels.
    rect(nodes, "jt-bg-solar", 70, 90, 1270, 850, "#EAFBFF")
    text(nodes, "jt-label-solar", "Trailer PV Sources", 110, 105, 34)
    rect(nodes, "jt-bg-battery", 1430, 90, 850, 1040, "#EEFDF2")
    text(nodes, "jt-label-battery", "48 V Battery / DC Cabinet", 1470, 105, 34)
    rect(nodes, "jt-bg-loads", 2370, 90, 880, 1040, "#FFF6E8")
    text(nodes, "jt-label-loads", "24 V / 12 V Loads", 2420, 105, 34)
    rect(nodes, "jt-bg-island", 70, 1210, 1600, 420, "#F8FAFC")
    text(nodes, "jt-label-island", "Standalone C1000 Island", 110, 1225, 34)
    rect(nodes, "jt-bg-notes", 1790, 1210, 1460, 420, "#F8FAFC")
    text(nodes, "jt-label-notes", "Guardrails", 1830, 1225, 34)

    # Solar strings.
    for i, x in enumerate((120, 340, 560), start=1):
        solar_panel(nodes, f"jt-roof-panel-{i}", f"Roof LG455 #{i}", x, 250)
    mcb_double(nodes, "jt-roof-pv-breaker", "Roof PV disconnect\n20 A / 250 V class", 815, 320, 20, 250)
    mppt(nodes, "jt-mppt-250-60", "Victron SmartSolar\n250/60-Tr", 1060, 250, 60, 250)

    for i, x in enumerate((120, 340), start=1):
        solar_panel(nodes, f"jt-ground-panel-{i}", f"Ground LG455 #{i}", x, 680)
    mcb_double(nodes, "jt-ground-pv-breaker", "Ground PV disconnect\n20 A / 150 V class", 815, 730, 20, 150)
    mppt(nodes, "jt-mppt-150-35", "Victron SmartSolar\n150/35", 1060, 660, 35, 150)

    # 48 V cabinet.
    busbar(nodes, "jt-pos-bus", "48 V Positive Busbar", "DC+", 1700, 400)
    busbar(nodes, "jt-neg-bus", "48 V Negative Busbar", "DC-", 1700, 650)
    battery(nodes, "jt-battery", 1700, 1000)
    class_t(nodes, "jt-main-fuse", "Main Class-T\nOCP TBD", 1910, 860, 125)
    shunt(nodes, "jt-shunt", 1490, 865)
    ground_point(nodes, "jt-dc-ground", "DC Ground Point", 1430, 650)

    breaker(nodes, "jt-velit-breaker", "Velit branch\nOCP TBD", 2170, 330, 20)
    custom_dc(nodes, "jt-velit", "Velit 2000R\n48 V rooftop AC", 2520, 310, "48 V", "5-14 A", "~670 W", 320, 160)

    breaker(nodes, "jt-orion24-input-breaker", "48/24 input\n20 A breaker", 2170, 560, 20)
    dcdc(nodes, "jt-orion-48-24", "Victron Orion-Tr\n48/24-16A isolated", 2520, 500, 48, 24, 16, 384)
    fusebox(nodes, "jt-blue-sea-5026", "Blue Sea 5026\n24 V fuse block", 2960, 510, 12)

    breaker(nodes, "jt-orion12-input-breaker", "48/12 input\nOCP TBD", 2170, 835, 10)
    dcdc(nodes, "jt-orion-48-12", "Victron Orion-Tr IP43\n48/12-20A isolated", 2520, 795, 48, 12, 20, 240)
    custom_dc(nodes, "jt-12v-receptacles", "12 V cabinet\nreceptacles only", 2960, 850, "12.2 V", "20 A max", "240 W", 300, 150)

    # Loads fed by the 24 V block.
    custom_dc(nodes, "jt-fridge", "Dometic CFX3 95DZ\nfridge", 3330, 330, "24 V", "4.6 A run", "1.0-1.3 kWh/day", 320, 145)
    custom_dc(nodes, "jt-lighting", "Interior / exterior\nlighting zones", 3330, 515, "24 V", "2-3 A int.; 5.25 A floods; 2.7 A awning", "", 360, 170)
    custom_dc(nodes, "jt-usb-gps-landairsea", "USB-C PD / GPS /\nLandAirSea", 3330, 720, "24 V", "USB up to 5 A; LandAirSea GPS <0.1 A", "", 360, 170)
    custom_dc(nodes, "jt-heater-topup", "Heater rough-in /\noptional C1000 top-up", 3330, 930, "24 V", "heater glow up to 11 A; top-up 10 A max", "shed first", 380, 170)

    # Standalone C1000 island.
    solar_panel(nodes, "jt-ps400", "Anker PS400", 140, 1390, 400)
    custom_dc(
        nodes,
        "jt-c1000",
        "Anker SOLIX C1000\nportable power station",
        550,
        1360,
        "11-60 V input",
        "12.5 A high-range / 10 A low-range",
        "1800 W AC",
        420,
        220,
        [
            port("jt-c1000", "pv-plus", "left", "PV+", 2),
            port("jt-c1000", "pv-minus", "left", "PV-", 3),
            port("jt-c1000", "ac-l", "right", "L", 0),
            port("jt-c1000", "ac-n", "right", "N", 1),
            port("jt-c1000", "ac-pe", "right", "PE", 2),
        ],
    )
    custom_dc(
        nodes,
        "jt-small-ac-loads",
        "Small AC / Starlink Mini\nlaptops, radios, chargers",
        1110,
        1370,
        "120 VAC island",
        "Starlink 25-40 W avg if used",
        "0.7-1.1 kWh/day if 24/7",
        420,
        190,
        [
            port("jt-small-ac-loads", "ac-l", "left", "L", 2),
            port("jt-small-ac-loads", "ac-n", "left", "N", 3),
            port("jt-small-ac-loads", "ac-pe", "left", "PE", 4),
        ],
    )

    text(
        nodes,
        "jt-note-guardrails",
        "PV guardrail: roof 3S, ground 2S, and PS400 are separate sources. "
        "Never combine them on one tracker.\n"
        "24 V load guardrail: C1000 top-up, full USB-C, all-flood mode, and heater glow are managed loads.",
        1840,
        1310,
        26,
    )

    # Current annotations are represented as text nodes because the reference
    # wire schema has size fields but no native wire-label/current fields.
    lead_label(nodes, "jt-label-roof-pv-current", "10.83 A MPP\n11.39 A Isc", 650, 505)
    lead_label(nodes, "jt-label-ground-pv-current", "10.83 A MPP\n11.39 A Isc", 650, 935)
    lead_label(nodes, "jt-label-mppt250-current", "24-28 A expected\n60 A limit", 1380, 455)
    lead_label(nodes, "jt-label-mppt150-current", "16-19 A expected\n35 A limit", 1380, 760)
    lead_label(nodes, "jt-label-pack-current", "<=100 A pack", 1830, 795)
    lead_label(nodes, "jt-label-velit-current", "5-14 A @ 48 V", 2360, 270)
    lead_label(nodes, "jt-label-orion24-input-current", "~9.2 A in", 2360, 515)
    lead_label(nodes, "jt-label-orion24-output-current", "16 A max @ 24 V", 2840, 615)
    lead_label(nodes, "jt-label-orion12-input-current", "~5.8 A in", 2360, 790)
    lead_label(nodes, "jt-label-orion12-output-current", "20 A @ 12 V", 2830, 905)
    lead_label(nodes, "jt-label-c1000-topup-current", "10 A max @ 24 V", 1490, 1265)
    lead_label(nodes, "jt-label-ps400-current", "8.33 A operating", 400, 1435)

    # Solar series and MPPT wiring.
    wire(wires, "jt-wire-roof-p1-minus-p2-plus", "jt-roof-panel-1", "jt-roof-panel-1-pv-minus", "jt-roof-panel-2", "jt-roof-panel-2-pv-plus", 6, [(260, 560), (400, 560)])
    wire(wires, "jt-wire-roof-p2-minus-p3-plus", "jt-roof-panel-2", "jt-roof-panel-2-pv-minus", "jt-roof-panel-3", "jt-roof-panel-3-pv-plus", 6, [(480, 560), (620, 560)])
    wire(wires, "jt-wire-roof-string-plus-breaker", "jt-roof-panel-1", "jt-roof-panel-1-pv-plus", "jt-roof-pv-breaker", "jt-roof-pv-breaker-pv-plus-in", 6, [(210, 610), (850, 610)])
    wire(wires, "jt-wire-roof-string-minus-breaker", "jt-roof-panel-3", "jt-roof-panel-3-pv-minus", "jt-roof-pv-breaker", "jt-roof-pv-breaker-pv-minus-in", 6, [(650, 600), (890, 600)])
    wire(wires, "jt-wire-roof-breaker-mppt-plus", "jt-roof-pv-breaker", "jt-roof-pv-breaker-pv-plus-out", "jt-mppt-250-60", "jt-mppt-250-60-pv-plus", 6, [(900, 470), (1110, 470)])
    wire(wires, "jt-wire-roof-breaker-mppt-minus", "jt-roof-pv-breaker", "jt-roof-pv-breaker-pv-minus-out", "jt-mppt-250-60", "jt-mppt-250-60-pv-minus", 6, [(930, 490), (1140, 490)])

    wire(wires, "jt-wire-ground-p1-minus-p2-plus", "jt-ground-panel-1", "jt-ground-panel-1-pv-minus", "jt-ground-panel-2", "jt-ground-panel-2-pv-plus", 6, [(260, 990), (400, 990)])
    wire(wires, "jt-wire-ground-plus-breaker", "jt-ground-panel-1", "jt-ground-panel-1-pv-plus", "jt-ground-pv-breaker", "jt-ground-pv-breaker-pv-plus-in", 6, [(210, 1040), (850, 1040)])
    wire(wires, "jt-wire-ground-minus-breaker", "jt-ground-panel-2", "jt-ground-panel-2-pv-minus", "jt-ground-pv-breaker", "jt-ground-pv-breaker-pv-minus-in", 6, [(430, 1020), (890, 1020)])
    wire(wires, "jt-wire-ground-breaker-mppt-plus", "jt-ground-pv-breaker", "jt-ground-pv-breaker-pv-plus-out", "jt-mppt-150-35", "jt-mppt-150-35-pv-plus", 6, [(900, 880), (1110, 880)])
    wire(wires, "jt-wire-ground-breaker-mppt-minus", "jt-ground-pv-breaker", "jt-ground-pv-breaker-pv-minus-out", "jt-mppt-150-35", "jt-mppt-150-35-pv-minus", 6, [(930, 900), (1140, 900)])

    # MPPT outputs to 48 V bus.
    wire(wires, "jt-wire-mppt250-pos-bus", "jt-mppt-250-60", "jt-mppt-250-60-dc-plus-a", "jt-pos-bus", "jt-pos-bus-top-0", 16, [(1350, 500), (1700, 500)])
    wire(wires, "jt-wire-mppt250-neg-bus", "jt-mppt-250-60", "jt-mppt-250-60-dc-minus-a", "jt-neg-bus", "jt-neg-bus-top-0", 16, [(1320, 620), (1700, 620)])
    wire(wires, "jt-wire-mppt150-pos-bus", "jt-mppt-150-35", "jt-mppt-150-35-dc-plus-a", "jt-pos-bus", "jt-pos-bus-top-1", 10, [(1370, 720), (1620, 520)])
    wire(wires, "jt-wire-mppt150-neg-bus", "jt-mppt-150-35", "jt-mppt-150-35-dc-minus-a", "jt-neg-bus", "jt-neg-bus-top-1", 10, [(1340, 810), (1620, 680)])

    # Battery, main fuse, shunt, and ground.
    wire(wires, "jt-wire-battery-plus-main-fuse", "jt-battery", "jt-battery-dc-plus", "jt-main-fuse", "jt-main-fuse-dc-plus-in", 35, [(1900, 980)])
    wire(wires, "jt-wire-main-fuse-pos-bus", "jt-main-fuse", "jt-main-fuse-dc-plus-out", "jt-pos-bus", "jt-pos-bus-bottom-0", 35, [(1900, 710), (1780, 560)])
    wire(wires, "jt-wire-battery-minus-shunt", "jt-battery", "jt-battery-dc-minus", "jt-shunt", "jt-shunt-dc-minus-in", 35, [(1560, 980)])
    wire(wires, "jt-wire-shunt-neg-bus", "jt-shunt", "jt-shunt-dc-minus-out", "jt-neg-bus", "jt-neg-bus-bottom-0", 35, [(1560, 760), (1720, 760)])
    wire(wires, "jt-wire-neg-bus-ground", "jt-neg-bus", "jt-neg-bus-ground", "jt-dc-ground", "jt-dc-ground-chassis-right-a", 16, [(1560, 650)])

    # 48 V branches.
    wire(wires, "jt-wire-pos-bus-velit-breaker", "jt-pos-bus", "jt-pos-bus-top-2", "jt-velit-breaker", "jt-velit-breaker-dc-plus-in", 4, [(2100, 410)])
    wire(wires, "jt-wire-velit-breaker-load-plus", "jt-velit-breaker", "jt-velit-breaker-dc-plus-out", "jt-velit", "jt-velit-dc-plus", 4, [(2380, 350)])
    wire(wires, "jt-wire-neg-bus-velit", "jt-neg-bus", "jt-neg-bus-top-2", "jt-velit", "jt-velit-dc-minus", 4, [(2100, 665), (2380, 430)])

    wire(wires, "jt-wire-pos-bus-orion24-breaker", "jt-pos-bus", "jt-pos-bus-top-3", "jt-orion24-input-breaker", "jt-orion24-input-breaker-dc-plus-in", 4, [(2100, 555)])
    wire(wires, "jt-wire-orion24-breaker-input-plus", "jt-orion24-input-breaker", "jt-orion24-input-breaker-dc-plus-out", "jt-orion-48-24", "jt-orion-48-24-in-plus", 4, [(2370, 555)])
    wire(wires, "jt-wire-neg-bus-orion24-input", "jt-neg-bus", "jt-neg-bus-top-3", "jt-orion-48-24", "jt-orion-48-24-in-minus", 4, [(2250, 675), (2550, 610)])

    wire(wires, "jt-wire-orion24-output-plus-fusebox", "jt-orion-48-24", "jt-orion-48-24-out-plus", "jt-blue-sea-5026", "jt-blue-sea-5026-input-plus", 4, [(2770, 650), (3020, 650)])
    wire(wires, "jt-wire-orion24-output-minus-fusebox", "jt-orion-48-24", "jt-orion-48-24-out-minus", "jt-blue-sea-5026", "jt-blue-sea-5026-input-minus", 4, [(2770, 720), (3020, 720)])

    wire(wires, "jt-wire-pos-bus-orion12-breaker", "jt-pos-bus", "jt-pos-bus-bottom-1", "jt-orion12-input-breaker", "jt-orion12-input-breaker-dc-plus-in", 2.5, [(2070, 830)])
    wire(wires, "jt-wire-orion12-breaker-input-plus", "jt-orion12-input-breaker", "jt-orion12-input-breaker-dc-plus-out", "jt-orion-48-12", "jt-orion-48-12-in-plus", 2.5, [(2360, 830)])
    wire(wires, "jt-wire-neg-bus-orion12-input", "jt-neg-bus", "jt-neg-bus-bottom-1", "jt-orion-48-12", "jt-orion-48-12-in-minus", 2.5, [(2240, 780), (2540, 900)])
    wire(wires, "jt-wire-orion12-output-plus-receptacles", "jt-orion-48-12", "jt-orion-48-12-out-plus", "jt-12v-receptacles", "jt-12v-receptacles-dc-plus", 4, [(2790, 940)])
    wire(wires, "jt-wire-orion12-output-minus-receptacles", "jt-orion-48-12", "jt-orion-48-12-out-minus", "jt-12v-receptacles", "jt-12v-receptacles-dc-minus", 4, [(2790, 990)])

    # 24 V branch loads from fuse box.
    load_pairs = [
        ("jt-fridge", "right-plus-0", "right-minus-0", 2.5),
        ("jt-lighting", "right-plus-1", "right-minus-1", 6),
        ("jt-usb-gps-landairsea", "right-plus-2", "right-minus-2", 2.5),
        ("jt-heater-topup", "right-plus-3", "right-minus-3", 6),
    ]
    for load_id, plus_port, minus_port, size in load_pairs:
        wire(wires, f"jt-wire-fusebox-{load_id}-plus", "jt-blue-sea-5026", f"jt-blue-sea-5026-{plus_port}", load_id, f"{load_id}-dc-plus", size)
        wire(wires, f"jt-wire-fusebox-{load_id}-minus", "jt-blue-sea-5026", f"jt-blue-sea-5026-{minus_port}", load_id, f"{load_id}-dc-minus", size)

    # C1000 island and optional 24 V top-up.
    wire(wires, "jt-wire-ps400-c1000-plus", "jt-ps400", "jt-ps400-pv-plus", "jt-c1000", "jt-c1000-pv-plus", 6, [(390, 1500)])
    wire(wires, "jt-wire-ps400-c1000-minus", "jt-ps400", "jt-ps400-pv-minus", "jt-c1000", "jt-c1000-pv-minus", 6, [(390, 1535)])
    wire(wires, "jt-wire-c1000-ac-l", "jt-c1000", "jt-c1000-ac-l", "jt-small-ac-loads", "jt-small-ac-loads-ac-l", 2.5)
    wire(wires, "jt-wire-c1000-ac-n", "jt-c1000", "jt-c1000-ac-n", "jt-small-ac-loads", "jt-small-ac-loads-ac-n", 2.5)
    wire(wires, "jt-wire-c1000-ac-pe", "jt-c1000", "jt-c1000-ac-pe", "jt-small-ac-loads", "jt-small-ac-loads-ac-pe", 2.5)
    wire(wires, "jt-wire-c1000-topup-plus", "jt-blue-sea-5026", "jt-blue-sea-5026-left-plus-0", "jt-c1000", "jt-c1000-dc-plus", 4, [(2840, 1260), (760, 1260)])
    wire(wires, "jt-wire-c1000-topup-minus", "jt-blue-sea-5026", "jt-blue-sea-5026-left-minus-0", "jt-c1000", "jt-c1000-dc-minus", 4, [(2820, 1290), (740, 1290)])

    return {
        "nodes": nodes,
        "wires": wires,
        "version": 1,
        "projectName": "Juplaya Trailer Power System",
    }


def validate(diagram: dict[str, Any]) -> None:
    required_top = {"nodes", "wires", "version", "projectName"}
    missing = required_top - set(diagram)
    if missing:
        raise SystemExit(f"missing top-level keys: {sorted(missing)}")

    node_ids: set[str] = set()
    port_ids: dict[str, set[str]] = {}
    for n in diagram["nodes"]:
        for key in ("id", "type", "x", "y", "ports", "data"):
            if key not in n:
                raise SystemExit(f"node missing {key}: {n}")
        if n["id"] in node_ids:
            raise SystemExit(f"duplicate node id: {n['id']}")
        node_ids.add(n["id"])
        port_ids[n["id"]] = set()
        for p in n["ports"]:
            for key in ("id", "side", "kind", "index"):
                if key not in p:
                    raise SystemExit(f"port missing {key}: {p}")
            if p["id"] in port_ids[n["id"]]:
                raise SystemExit(f"duplicate port id on {n['id']}: {p['id']}")
            port_ids[n["id"]].add(p["id"])

    wire_ids: set[str] = set()
    for w in diagram["wires"]:
        for key in ("id", "sourceNodeId", "sourcePortId", "targetNodeId", "targetPortId", "midpoints", "routingMode"):
            if key not in w:
                raise SystemExit(f"wire missing {key}: {w}")
        if w["id"] in wire_ids:
            raise SystemExit(f"duplicate wire id: {w['id']}")
        wire_ids.add(w["id"])
        if w["sourceNodeId"] not in node_ids:
            raise SystemExit(f"wire {w['id']} has unknown source node {w['sourceNodeId']}")
        if w["targetNodeId"] not in node_ids:
            raise SystemExit(f"wire {w['id']} has unknown target node {w['targetNodeId']}")
        if w["sourcePortId"] not in port_ids[w["sourceNodeId"]]:
            raise SystemExit(f"wire {w['id']} has unknown source port {w['sourcePortId']}")
        if w["targetPortId"] not in port_ids[w["targetNodeId"]]:
            raise SystemExit(f"wire {w['id']} has unknown target port {w['targetPortId']}")


def main() -> int:
    diagram = build()
    validate(diagram)
    OUT.write_text(json.dumps(diagram, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT} ({len(diagram['nodes'])} nodes, {len(diagram['wires'])} wires)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
