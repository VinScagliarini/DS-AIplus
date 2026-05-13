# AI+ Ecosystem · brand index

L'umbrella brand AI+ Ecosystem è composto da 9 brand verticali. Tutti
condividono la stessa grammatica visiva (badge a gradient diagonale,
tipografia MuseoModerno + Roboto, lockup *AI+* e *powered by logotel*) e
si differenziano per **hue brand** e posizionamento.

## Schema visivo condiviso

- **Forma**: card 1:1 con angoli `1.75rem`
- **Background**: gradient lineare 135° da `#F7F6F3` (cream) → soft brand
- **Wordmark**: `MuseoModerno Medium` uppercase, color `--brand-ink-deep`
- **Bottom-left**: lockup `AI+` (MuseoModerno SemiBold)
- **Bottom-right**: lockup `powered by logotel` (Roboto Regular + MuseoModerno)

## I 9 brand

| Brand | Hue | Soft | Primary | Posizionamento |
|---|---|---|---|---|
| [JUMP](./brands/jump.md) | mint | `#BEF6D3` | `#56E3B0` | Activation enablement |
| [HIVE](./brands/hive.md) | amber | `#FAD08E` | `#FDB84B` | Network intelligence |
| [WILLSELL](./brands/willsell.md) | cyan | `#A6F1F3` | `#06CBD2` | AI sales coach |
| [DOJO](./brands/dojo.md) | yellow | `#F9E590` | `#FBD947` | Continuous training |
| [CREATIVE STUDIO](./brands/creative-studio.md) | magenta | `#F0BEF7` | `#D464F0` | Creative production |
| [MAINDSET](./brands/maindset.md) | violet | `#BFB8FA` | `#968CFF` | AI culture |
| [LEADAI](./brands/leadai.md) | coral | `#F4ABA6` | `#F2746F` | AI lead generation |
| [REFRAMING LAB](./brands/changelab.md) | blue | `#95B5FA` | `#568BFF` | Change as experiment |
| [LIVE AI+](./brands/liveai-plus.md) | lime | `#BBF0AD` | `#95EC80` | Live experience |

## Come selezionare un brand

```html
<!-- Vanilla HTML/CSS -->
<html data-brand="creative-studio">
```

```jsx
// React/Next con Tailwind preset
<div className="brand-creative-studio">
  <h1 className="text-brand">Creatività alla velocità degli algoritmi</h1>
</div>
```

```js
// Programmatic
document.documentElement.setAttribute('data-brand', 'creative-studio');
```

Il selettore `[data-brand="<slug>"]` (o la classe `.brand-<slug>`) imposta
le custom property `--brand-*` sul subtree, così componenti di sistema
(`.ds-hero`, `.ds-badge`, `.ds-button`, ...) ereditano automaticamente la
palette giusta.
