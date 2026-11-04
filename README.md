# Git-lopputyö – Python-laskin

## Projektin idea

Tässä lopputyössä tein yksinkertaisen Python-laskimen, jolla voi laskea yhteen-, vähennys-, kerto- ja jakolaskuja. Ohjelma toimii terminaalissa, ja käyttäjä valitsee haluamansa laskutoimituksen valikosta.

Laskimessa on myös virheenkäsittely, eli ohjelma ei kaadu, jos käyttäjä syöttää jotain muuta kuin numeroita tai yrittää jakaa nollalla.

Itse ohjelma on aika yksinkertainen, koska tässä työssä tarkoituksena oli enemmänkin harjoitella Gitin käyttöä kuin tehdä mitään monimutkaista Python-ohjelmaa.

## Gitin käyttö projektissa

Tein projektin PyCharmilla ja käytin Git-komentoihin PyCharmin PowerShell-terminaalia. GitHub-yhteyden muodostin SSH:lla.
Projektin aikana tuli käytettyä seuraavia komentoja:

| Komento | Mihin käytin |
|---|---|
| `git clone` | Repositorion kloonaaminen GitHubista |
| `git status` | Muutosten ja nykyisen tilanteen tarkistaminen |
| `git add` | Tiedostojen lisääminen staging-alueelle |
| `git commit` | Muutosten tallentaminen Gitin historiaan |
| `git push` | Muutosten lähettäminen GitHubiin |
| `git pull --ff-only` | GitHubissa tehtyjen muutosten hakeminen |
| `git switch` | Haarojen välillä liikkuminen |
| `git switch -c` | Uuden haaran luominen |
| `git branch` | Haarojen tarkistaminen |
| `git merge` | Haarojen yhdistäminen |
| `git stash` | Keskeneräisten muutosten laittaminen talteen |
| `git stash pop` | Tallennettujen muutosten palauttaminen |
| `git rebase main` | Feature-haaran päivittäminen main-haaran päälle |
| `git revert` | Virheellisen commitin peruuttaminen |
| `git cherry-pick` | Yksittäisen commitin kopioiminen toisesta haarasta |
| `git tag` | Version merkitseminen |
| `git log` | Commit-historian tarkastelu |
| `git check-ignore` | .gitignore-tiedoston toiminnan tarkistaminen |

## Haarat ja niiden yhdistäminen

Tein laskimen toimintoja eri feature-haaroissa. Ensimmäisenä tein `feature/addition`-haaran, jossa toteutin yhteenlaskun. Sen jälkeen tein `feature/subtraction`-haaran vähennyslaskua varten.

Yhdistin ensin yhteenlaskun main-haaraan. Tämän jälkeen päivitin vähennyslaskuhaaran `git rebase main` -komennolla.

Myöhemmin tein myös `feature/multiplication`-haaran ja kopioin sen commitin `git cherry-pick` -komennolla `feature/calculator-update`-haaraan. Samassa haarassa toteutin vielä jakolaskun.

Lopuksi tein GitHubissa Pull Requestin, jonka kautta yhdistin kertolaskun ja jakolaskun main-haaraan.

## Merge-konflikti

Yksi ongelma tuli vastaan `git rebase main` -komennon kanssa.

Olin lisännyt yhteenlasku- ja vähennyslaskufunktiot eri haaroissa samaan kohtaan `main.py`-tiedoston alkuun. Kun yritin päivittää vähennyslaskuhaaraa, Git ei osannut automaattisesti yhdistää muutoksia.

Ratkaisin konfliktin PyCharmissa poistamalla konfliktimerkinnät ja säilyttämällä molemmat funktiot. Myös valikon muutokset piti tarkistaa, jotta molemmat laskutoimitukset toimivat.

Tämän jälkeen käytin komentoja `git add main.py` ja `git rebase --continue`, jolloin rebase meni onnistuneesti loppuun.

## Stash-harjoitus

Kokeilin myös `git stash` -komentoa.

Lisäsin `main.py`-tiedostoon väliaikaisen TODO-kommentin ja tallensin muutoksen stashilla. Tarkistin `git status` -komennolla, että työhakemisto oli jälleen puhdas.

Sen jälkeen palautin muutoksen `git stash pop` -komennolla. Kommentti palautui tiedostoon ja stash-lista tyhjeni.

Lopuksi poistin väliaikaisen kommentin.

## Virheellisen commitin peruuttaminen

Harjoittelin `git revert` -komentoa tekemällä tarkoituksella virheen yhteenlaskufunktioon. Muutin sen laskemaan vähennyslaskun ja tallensin muutoksen committiin.

Tämän jälkeen peruin virheellisen commitin `git revert` -komennolla.

Huomasin, että revert ei poista vanhaa committia historiasta, vaan tekee uuden commitin, joka kumoaa muutoksen. Näin myös virheellinen commit jää näkyviin Gitin historiaan.

## Cherry-pick

Kertolaskun toteutin ensin omassa `feature/multiplication`-haarassa.

Sen jälkeen loin `feature/calculator-update`-haaran mainista ja käytin `git cherry-pick` -komentoa kertolaskun commitin kopioimiseen.

Commit sai uuden tunnisteen, vaikka sen sisältämät muutokset olivat samat. Näin pystyin siirtämään yksittäisen muutoksen toiseen haaraan ilman koko haaran yhdistämistä.

## .gitignore ja versiotagi

Lisäsin projektiin `.gitignore`-tiedoston, jotta esimerkiksi PyCharmin `.idea`-kansio ja Pythonin `.venv`-virtuaaliympäristö eivät päädy GitHubiin.

Testasin sen toiminnan `git check-ignore -v` -komennolla.

Kun laskimen kaikki toiminnot olivat valmiit, loin myös version `v1.0.0` ja lähetin tagin GitHubiin.

## Ongelmia matkan varrella

Alussa SSH-yhteys GitHubiin ei toiminut ollenkaan. Lopulta tajusin, että minulla oli VPN päällä, mikä esti yhteyden muodostamisen. Kun otin VPN:n pois päältä, yhteys alkoi toimia.

Sen jälkeen tuli vielä `Permission denied (publickey)` -virhe. Koneella ei ollut SSH-avainta, joten loin uuden avainparin ja lisäsin julkisen avaimen GitHubiin. Tämän jälkeen SSH-yhteys toimi normaalisti.

Toinen isompi ongelma oli rebasen yhteydessä tullut merge-konflikti. Sen selvittelyyn meni vähän aikaa, mutta samalla opin paremmin, mistä konfliktit syntyvät ja miten ne ratkaistaan.

## Mitä opin?

Aikaisemmin olin käyttänyt lähinnä Gitin peruskomentoja, kuten add, commit, push ja pull. Tässä tehtävässä pääsin kokeilemaan enemmän myös muita toimintoja.

Erityisesti rebase ja cherry-pick olivat uusia asioita. Aluksi niiden tarkoitus ei ollut ihan selvä, mutta käytännössä kokeilemalla ne alkoivat aueta.

Opin myös, miten Gitin haarat toimivat ja miksi muutoksia kannattaa tehdä erillisissä feature-haaroissa suoraan main-haaran muokkaamisen sijaan.

Merge-konfliktin ratkaiseminen oli ehkä hyödyllisin osa harjoitusta. Nyt ymmärrän paremmin, miksi konflikti voi syntyä ja miten Gitin lisäämät konfliktimerkinnät toimivat.
