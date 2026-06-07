# Diagram JSON Schema Notes

This is an inferred schema from `docs/reference/diagram.json`. No formal JSON
Schema file was present in the repository.

Top-level object:

- `version`: integer.
- `projectName`: string.
- `nodes`: array of node objects.
- `wires`: array of wire objects.

Node object:

- `id`: stable string identifier.
- `type`: renderer component type, for example `rect`, `text`, `solarPanel`,
  `solar`, `battery`, `busbar`, `fuse`, `mcb`, `mcb-double`, `dcdc`,
  `fusebox`, `custom`, `groundPoint`, or `inverter`.
- `x`, `y`: diagram coordinates.
- `ports`: array of port objects.
- `data`: renderer/component metadata. Common keys are `label`, `brand`,
  `category`, `componentId`, `width`, `height`, and `properties`.

Port object:

- `id`: stable string identifier.
- `side`: one of the rendered sides such as `top`, `bottom`, `left`, `right`.
- `kind`: electrical kind such as `DC+`, `DC-`, `PV+`, `PV-`, `L`, `N`, `PE`,
  `GND`, `CHASSIS`, or `SIG`.
- `index`: numeric ordering for ports on the same side.

Wire object:

- `id`: stable string identifier.
- `sourceNodeId`, `sourcePortId`: source node and port IDs.
- `targetNodeId`, `targetPortId`: target node and port IDs.
- `midpoints`: array of `{id, x, y}` routing points.
- `routingMode`: usually `auto` or `manual`.
- `wireSize`: numeric conductor size.
- `wireSizeUnit`: `mm2` in the reference file.
- `isAutoSized`: boolean.

Component metadata conventions:

- `componentId` selects the renderer component implementation, such as
  `monocrystalline-panel`, `mppt-controller`, `lithium-battery`,
  `positive-busbar`, `negative-busbar`, `dc-inline-breaker`, `dc-fuse-box`,
  `smart-charger-dcdc`, `custom-dc`, or `text`.
- `properties` is an array of displayable property objects with `id`, `name`,
  `value`, `visible`, and `isDefault`.
- The parser appears tolerant of project-specific labels and property values as
  long as node, port, and wire references are internally consistent.

Generated trailer artifact:

- `scripts/generate_juplaya_power_diagram_json.py` emits
  `docs/reference/juplaya-power-diagram.json` using this inferred schema.
- Estimated current annotations are represented as ordinary `text` nodes near
  the relevant leads because the sampled wire object has conductor-size fields
  but no native wire-label or current field.
