## info
- http://kmat.vse.cz
- Konzultace pro emailové domluvě

# Vektory a matice

## Aritmetický vektor
- Uspořádaná entice reálných čísel
  - Značí se jako a(šipka) = (a<sub>1</sub>, a<sub>2</sub>, ...,  a<sub>n</sub>)
- Čísla a<sub>1</sub>,... jsou složky / souřadnice vektoru a
- **Speciální případ** - nulový vektor. o(šipka). (0, 0, 0, 0, ... 0)
- Množina všech uspořádaných entic = **V<sub>n</sub>**
  - (3, -2) náleží V<sub>2</sub>
    - Index značí počet souřadnic


## Operace s vektory
- Definujeme několik operací
  - Vektory musí mít stejnou délku
  - Pak tam musí být ještě reálné číslo `c`
---
    Rovnost vektorů
    a = b když a<sub>1</sub> = b<sub>1</sub>
---
    Součet vektorů
    Součet odpovídajících prvků
    a + b = a1 + b1, a2 + b2
---
    Reálný násobek vektoru
    Každý prvek vynásobím `c`
    ca = (ca1, ca2, ca3,...)
---
  - Jestliže na množině V<sub>n</sub> definujeme součet vektorů a reálný náísobek vektoru, pak se V<sub>n</sub> nazývá **vektorový prostor**.
  - **Jednotkové vektory** - v prostoru V<sub>n</sub> je **n** jednotkových vektorů *(Je tam jedna jednička, zbytek jsou nuly)*
---
    Lineární kombinace vektorů
    x1, x2, ..., xp jsou vektory.
    ci náleží reálným číslům. Jsou to koeficienty
    c1*x1, c2*x2, cp*xp
    Pak to sečteme.
    c1*x1 + c2*x2 + cp*xp
    --> Součet reálných násobků vektorů
    Vektor x je **lineární kombinací** vektorů (z jednoho prostoru) jestliže existují reálná čísla c1, c2, cp, taková, že platí x = c*1*x1 + ... cp*xp
---
LK (lineární kombinace) se nazývá:
- **Triviální**, pokud jsou všechna `c` 0
  - Pak se při kombinaci zpravidla dostaneme na nulový vektor
- **Netriviální**, jestliže alespoň jedno `c` není 0
  
---
### Příklad:

Libovolná lineární kombinace, Je x3 LK x1 a x2<br>
x<sub>1</sub> = (3, 1) c1 = 6<br>
x<sub>2</sub> = (-2, 0) c2 = 0<br>
x<sub>3</sub> = (1, 5) c3 = 2<br>

c<sub>1</sub>x<sub>1</sub> + c<sub>2</sub>x<sub>2</sub> + c<sub>3</sub>x<sub>3</sub> = x<br>
6(3, 1) + 0(-2, 0) + 2(1, 5) = `(20, 16)`

<small>Teď si ty koeficienty nemůžeme zvolit</small><br>

c<sub>1</sub>x<sub>1</sub> + c<sub>2</sub>x<sub>2</sub> ?= x<sub>3</sub><br>

c<sub>1</sub>(3, 1) + c<sub>2</sub>(-2, 0) = (1, 5)<br>
(3c<sub>1</sub>, c<sub>1</sub>) + (-2c<sub>1</sub>, 0c<sub>2</sub>) = (1, 5)<br>
(3c<sub>1</sub> - 2c<sub>1</sub>, c<sub>1</sub> + 0) = (1, 5)<br>
<small>Můžu rozepsat po souřadnicích</small><br>
3c<sub>1</sub> - 2c<sub>2</sub> = 1<br>
c<sub>1</sub> = 5<br>
c<sub>2</sub> = 7<br>
... `ANO`<br>
Best practice je to pak napsat ještě za ta C

---
## Lineární závislost a nezávislost
    Vektory x1, ... xp jsou závislé, jestliže existuje jejich netriviální lineární kombinace, která je rovna nulovému vektoru.

V opačném případě jsou vektory lineárně nezávislé, tj <u>pouze</u> jejich <u>triviální</u> LK je rovna nulovému vektoru

... To dokazování je někdy zdlouhavé. Často postačuje oko. Therefore:
### Věta:
    Vektory x1 ... xp právě tehdy, když alespoň jeden z nich je lineární kombinací ostatních.
**Poznámky**
-  Jeden vektor x<sub>1</sub> je lineárně závislý právě tehdy, když je nulový x<sub>1</sub> = o
- Dva vektory x<sub>1</sub>, x<sub>2</sub> jsou LZ právě tehdy, když jeden je reálným násobkem druhého.
  - x<sub>1</sub>= cx<sub>2</sub>
- Obsahuje-li skupinka vektorů nulový vektor, je LZ. (dá se vyjádřit jako triviální lineární kombinace)
- Pokud jsou dva stejné, tak jsou závislé.
- Pokud jsou to násobky, je to taky ok.

# Matice
- Matice typu m x n je schéma reálných čísel uspořádaných do m řádků a n sloupců.
- Značíme [a<sub>ij</sub>], kde `i` je řádek a `j` sloupec
- Každý řádek / sloupec je de facto vektor
  - De facto řádkové vektory a sloupcové vektory
- Bere se i diagonála. a<sub>11</sub>, a<sub>22</sub>,...
  - Diagonální prvky, hlavní diagonála matice

**Speciální případy**
- Nulová matice -> značí se **O**
- Všechny prvky jsou 0
- Pokud je m == n, pak se říká, že matice je **čtvercová** řádu `n`

## Jednotková matice
    - Týká se jen čtvercové matice
    - Značí se `J`
    - Čtvercová matice J čádu n, pro jejíž prvky platí i, j = 1, ... , n
    - aii = 1
    - aij = 0 pro i!=j
    - se nazývá jednotková matice

-- Basically má jedničky jen na diagonále. Řádky tvoří jednotkové vektory.

    Matice A a B typu m x n jsou si rovny (A = B), jestliže pro všechna i = 1, ... , m a j= 1, ... , n platí aij = bij

## Trojúhelníková matice
    Matice typu m x n se nazývá trojúhelníková, když m <= n a platí:

    ajj != 0 pro i = 1, ... m
    aij = 0 pro j < i

-- Všechno pod diagonálou je nula.
- Je tam charakteristické rozložení nul. 1. řádek = 0 nul, 2. řádek = 1 nula,...

## Schodovitá matice
- Počet nul na začátku může přiskočit víc, než u trojúhelníku. Nemusí to být pouze 1, klidně i víc.
- Už se neřeší i diagonála

## Hodnost matice
    Maximální počet lineárně nezávislých řádků matice A. Značí se písmenkem h(A) / jen h.

- Až na výjimky to bude přirozené číslo.
- Nulová matice má hodnost 0.
- Jestliže je matice v trojúhelníkovém tvaru, pak je její hodnost rovna počtu řádků.

*Příklad*
- Pokud budu mít matici 3 x 5, tak h je maximálně 3.
- Pokud budu mít matici 7 x 4, tak h je maximálně 4.

## Elementární úpravy matice
- Nemění hodnost.
1. Vyměníme pořadí řádků
2. Vynásobíme libovolný řádek nenulovým číslem
3. K jednomu řádku můžeme přičíst lineární kombinaci ostatních (většinou násobek)
4. Vynecháme řádek, který je LK ostatních (typicky nulové vektorové řádky)
5. (Zaměníme pořadí sloupců) -- většinou to není nutné. Hodnost lze poznat i v odstupňovaném tvaru - nenulové řádky.

## LZ a LNZ využitím hodnosti matice
    Mějme p vektorů z Vn. Vytvořme matici tak, že dané vektory jsou jejími řádky.
Pak platí, že:

- h = p (Ani jeden řádek není vyškrtnutý) Všechno je lineárně nezávislé
- h < p Vektory jako celek jsou lineárně závislé.

## Transponovaná matice
    Matice A`, která vznikne z A tak, že zaměníme řádky za sloupce, přičemž zachováme jejich pořadí, se nazývá matice transponovaná k matici A.
