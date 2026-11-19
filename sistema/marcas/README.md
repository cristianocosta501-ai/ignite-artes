# Perfis de marca

Cada arquivo `<slug>.json` guarda cor e fonte de uma marca, sempre por papel
(`papel`, `tinta`, `apagado`, `destaque`, `destaque_texto`, `linha`, `link`).
Diagramas e peças chamam o papel, nunca o hex solto.

## Como escolher o perfil num projeto
Na pasta do projeto, crie um arquivo `.marca` com uma linha:

```
perfil: ignite
```

## Perfil de cliente novo
1. Fonte: manual de marca (vence sempre) ou leitura de 2 a 3 páginas do site, com aprovação antes de acessar.
2. Validar: tinta sobre papel >= 4,5:1; destaque usado como texto >= 4,5:1 (senão criar `destaque_texto` mais escuro).
3. Marcar cada fonte como `exata` ou `substituta`.
4. Gravar só depois de aprovar uma peça de prova.

Peça final de cliente nunca sai com o perfil `ignite`.

## Conferência de layout
`python3 sistema/conferir_layout.py peca.html --largura 1080 --altura 1350`
(story/Reel: `--altura 1920 --topo 250 --base 380`). Marque no HTML
`data-protegido` no título, `data-caixa` nos cartões e `data-livre` nos adesivos.
