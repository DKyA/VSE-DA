# Soustavy lineárních rovnic v maticích
- V podstatě se jenom přepíše do matice
  - Ano, jsem línej to psát
---
    Tvoří se "matice soustavy"
---
    Rozšířená matice soustavy = matice soustavy + svislá čára, za tou jsou pravé strany (jen čísla)
---
> A<sub>r</sub> = [1 2 3 | 4] => x + y + z = 4

- Opět se počítají hodnost matic
- h = h(A), h<sub>r</sub> = h(A<sub>r</sub>)
- Jsou dvě možnosti:
  - h = h<sub>r</sub>
  - h < h<sub>r</sub> (h = h + 1)
  - Jsou buď stejné, nebo o 1 větší

## Možnosti řešení
- 1 (Právě 1 entice)
- 0
- Nekonečně mnoho (pi = pi)

### Jak řešit?
#### `Frobeniova` podmínka:
- `Soustava lineárních rovnic má řešení právě tehdy, když hodnost matice soustavy A se rovná hodnosti rozšířené matice soustavy A<sub>r</sub>`
- Z toho plyne, že pokud jsou hodnosti různé, soustava `nemá` řešení

#### Věta o `počtu řešení soustavy`
- Mějme soustavu lineárních rovnic a označme `h` hodnost soustavy, `n` bude počet neznámých. Má-li soustava linárních rovnic řešení *(h = h<sub>r</sub>)*, pak platí:
  - `h = n` => soustava má **právě 1 řešení**
  - `h < n` => soustava má **nekonečně mnoho** řešení
    - Za n - h neznámých lze volit libovolná reálná čísla, ostatní neznámé jsou určené jednoznačně. (= parametry)

Typy když vyjde neomezený počet řešení:
- **Obecné řešení**:
  - Popisuje všechna řešení dané soustavy
  - Za volitelné neznámé se volí obecné parametry
  - ČASTĚJŠÍ!!!
- **Partikulární řešení**
  - Každé jedno řešení z té množiny nekonečně mnoha
  - Dostaneme ho tak, že za volitelné neznámé volíme konkrétní reálná čísla

#### Věta o `ekvivalentních soustavách`
- Provedeme-li v rozšířené matici soustavy **elementární řádkové úpravy**, dostaneme rozšířenou matici soustavy, které odpovídá *ekvivalentní soustava* lineárních rovnic (má **stejnou** množinu řešení jako původní)

---
- Lepší dělat řádkové, než sloupcové úpravy. Proč?
  - Může se to plést. Co nejvíc používat řádkové.
- **Jediná povolená sloupcová úprava** => můžeme vyměnit sloupce.
  - Pozor, prohodí se pořadí neznámých, je dobré si to někde poznamenat

## Homogenní soustava lineárních rovnic
- Speciální případ
- Na pravých stranách jsou jen a pouze nuly
- Typicky úmyslný výsledek = zkrátí se to tak, aby tam byly nuly
- Platí pro ní vše, co platí pro obyčejné soustavy
    - Plus něco málo navíc

### Typy řešení
- Triviální
  - Všechny neznámé jsou 0
  - Vyjde nulový vektor
- Netriviální
  - Relativně běžnější
  - Aspoň jedna věc je číslo různé od 0

#### Věta o `počtu řešení homogenní soustavy`
- Homogenní soustava lineárních rovnic má vždy řešení.
- Označíme-li `h` hodnost matice soustavy, `n` počet neznámých, pak platí:
- **h = n** => soustava má právě 1 řešení
- **h < n** => soustava má nekonečně mnoho řešení (i netriviální). Za `n - h` neznámých lze volit parametr
- Při řešení není nutné pořád opakovat pravou stranu. Nemění se
