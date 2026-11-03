# Tiivistelmä


Havainnollistavan työn tavoitteena oli parantaa uudelleenyritysten käsittelyä kuvitteellisessa kampuksen tapahtumapalvelussa. Tarkoituksena oli estää saman tapahtuman tallentuminen kahdesti tilanteessa, jossa lähettäjä ei saanut ensimmäisen pyynnön vastausta.

Esimerkissä kuvattiin tekninen suunnittelututkimus ja kontrolloitu vertailuasetelma, tietokantatapahtumaan perustuva ratkaisu ja toiminnallisten tarkistusten suunnitelma. Synteettinen aineisto sisälsi 1 000 yksilöllistä tapahtumaa, 200 uudelleenyritystä ja viisi parittaista viiveyhteenvetoa. Sovellusta tai vertailutestiä ei todellisuudessa suoritettu.

Havainnollistavassa aineistossa suojattu ratkaisu sisälsi 1 000 tapahtumariviä, kun vertailuratkaisu sisälsi 1 200 riviä. Ajokohtaisten p95-viiveiden keskiarvo kasvoi 26 millisekunnista 30 millisekuntiin. Ristiriitaiset hyötykuormat ja peruutustilanteet kuvattiin erillisinä tarkistuksina, ei onnistuneina testituloksina.

Esimerkki havainnollisti pysyvän tapahtumatunnisteen, rajatun tallennusvastuun ja jäljitettävien arviointikriteerien yhteyttä. Laskelmat eivät osoittaneet tuotantojärjestelmän suorituskykyä, rinnakkaisten pyyntöjen turvallisuutta tai ulkoisen toimituksen takeita. Nämä kysymykset jäivät todellisessa toteutuksessa arvioitaviksi.