"""Générateur de la maquette Habitat Concept Intérieur (HCI). Usage : python build.py <dossier-du-projet>
Contenus relevés sur hcicuisines.fr, la fiche Google (photos du propriétaire, avis, horaires) et Facebook (13/11/2026).
Rien d'inventé : services, logo, couleurs, police Golos Text, photos de réalisations, avis, coordonnées.
Les visuels d'illustration du site actuel sont écartés : seules les photos publiées par l'entreprise sur Google sont utilisées."""
import os
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else "."
A = 'assets/'
PH = A + 'ph/'
V = 4  # cache : incrémenter à chaque changement de CSS ou JS
TEL, TELH = '04 74 47 19 76', 'tel:0474471976'
MAIL = 'contact@hcicuisines.fr'
ADR = ('200 avenue Clément Désormes', '01400 Châtillon-sur-Chalaronne')
FB = 'https://www.facebook.com/hcicuisines/'
NAV = [('cuisines.html', 'Cuisines'), ('amenagement.html', 'Bain & dressing'), ('realisations.html', 'Réalisations')]


def pill(t, href, cls='', arrow='↗'):
    return f'<a class="pill {cls}" href="{href}"><span class="r"><span>{t}</span><span>{t}</span></span><b>{arrow}</b></a>'


def tile(src, cls='', style='', alt='', par=None, lazy=True):
    p = f' data-par="{par}" style="height:118%;width:100%"' if par else ''
    return f'<figure class="tile {cls}" style="{style}"><img src="{src}" alt="{alt}"{p}{" loading=lazy" if lazy else ""}></figure>'


def logo(cls=''):
    return f'<span class="lgo {cls}" aria-hidden="true"><img src="{A}maison.png" alt=""><span><span class="wm">Habitat <b>Concept</b> Intérieur</span><small>Cuisine · Bain · Dressing</small></span></span>'


def head(title, desc, cur):
    def a(h, t, cls=''):
        return f'<a href="{h}"{" class="+cls if cls else ""}{" aria-current=page" if h == cur else ""}>{t}</a>'
    items = a('index.html', 'Accueil') + ''.join(a(h, t) for h, t in NAV) + a('contact.html', 'Devis gratuit', 'hl')
    return f'''<!doctype html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<meta name="theme-color" content="#0d0d0e">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="{A}maison.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Golos+Text:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{A}style.css?v={V}">
</head><body>
<div id="bar"></div>
<header class="top">
<a class="logo" href="index.html" aria-label="Habitat Concept Intérieur, accueil">{logo()}</a>
<nav class="nav" aria-label="Navigation principale"><button class="stop" type="button" aria-label="Fermer le menu"><span>MENU</span></button>{items}</nav>
<span class="side"><a class="tel" href="{TELH}" aria-label="Appeler le {TEL}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z" fill="currentColor"/></svg><span>{TEL}</span></a></span>
<button class="burger" aria-label="Menu" aria-expanded="false"><i></i><i></i></button>
</header>
<main>'''


def foot():
    return f'''</main>
<footer><div class="wrap"><div class="fg">
<div><img class="flogo" src="{A}logo.png" alt="Habitat Concept Intérieur"><p>Cuisines sur mesure, salles de bain, dressings et rénovation intérieure. Showroom à Châtillon-sur-Chalaronne.</p></div>
<div><h4 class="micro">Savoir-faire</h4><ul><li><a href="cuisines.html">Cuisines sur mesure</a></li><li><a href="amenagement.html">Salles de bain</a></li><li><a href="amenagement.html#dressing">Dressings et bibliothèques</a></li><li><a href="amenagement.html#renovation">Rénovation complète</a></li><li><a href="realisations.html">Réalisations</a></li></ul></div>
<div><h4 class="micro">Contact</h4><ul><li><a href="{TELH}">{TEL}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li><li><a href="contact.html">Devis gratuit</a></li><li><a href="{FB}" target="_blank" rel="noopener">Facebook</a></li></ul></div>
<div><h4 class="micro">Showroom</h4><ul><li>{ADR[0]}</li><li>{ADR[1]}</li><li>Lundi au vendredi, 9 h – 17 h</li></ul></div>
</div></div>
<div class="fw" aria-hidden="true">HCI</div>
<div class="fb micro"><span class="pad">© Habitat Concept Intérieur</span><span class="pad">Maquette de site · Le Génie Numérique</span></div></footer>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://unpkg.com/lenis@1.1.13/dist/lenis.min.js"></script>
<script src="{A}main.js?v={V}"></script></body></html>'''


def cta(t='Votre cuisine, <em>sur mesure</em> ?'):
    return f'''<section class="sec cta"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.6rem">Devis gratuit · showroom à Châtillon</span><h2 class="sp">{t}</h2>
<div class="row rv">{pill('Demander un devis', 'contact.html', 'blue')}{pill(TEL, TELH, 'ghost')}</div></div></section>'''


def pagehead(crumb, h1, lead, img, img2=None, extra=''):
    t2 = tile(img2, 'small', lazy=False) if img2 else ''
    return f'''<section class="ph"><div class="wrap"><div class="crumb micro"><a href="index.html">Accueil</a> / {crumb}</div><h1 class="sp">{h1}</h1><p class="lead rv">{lead}</p>{extra}</div>{tile(img, lazy=False)}{t2}</section>'''


def faq(its):
    return '<div class="faq">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in its) + '</div>'


# vraies réalisations (photos publiées par l'entreprise sur sa fiche Google)
GAL = [('cuisine-noyer', 'Cuisines', 'Cuisine ouverte, îlot et colonnes bois'), ('salle-de-bain', 'Bain', 'Salle de bain, douche à l’italienne'),
       ('cuisine-ilot', 'Cuisines', 'Cuisine en U, bois clair et façades grises'), ('bibliotheque', 'Rangements', 'Bibliothèque murale sur mesure'),
       ('cuisine-bois-clair', 'Cuisines', 'Cuisine en L, décor bois clair'), ('ilot-gris', 'Cuisines', 'Îlot gris anthracite, plan bois'),
       ('cuisine-blanche', 'Cuisines', 'Cuisine blanche, plan de travail chêne'), ('cuisine-grise', 'Cuisines', 'Cuisine grise, colonnes four'),
       ('cuisine-plan-beton', 'Cuisines', 'Plan de travail effet béton, niche éclairée'), ('cuisine-gris-bois', 'Cuisines', 'Cuisine gris et bois, coin repas'),
       ('salle-a-manger', 'Rangements', 'Coin repas et rangements assortis'), ('showroom', 'Showroom', 'Le showroom, avenue Clément Désormes')]

AVIS = [('Evelyne', 'Novembre 2026', 'Beaucoup de rangement bien pensé et très bonne qualité. Personnel très réactif et un suivi génialissime.'),
        ('Héloïs', 'Mai 2026', 'Du début à la fin, j’ai été accompagnée avec beaucoup de sérieux et de professionnalisme par Fabrice et son équipe.'),
        ('Denis', '2025', 'Leur équipe a créé la cuisine que je voulais alors que beaucoup d’autres cuisinistes avaient renoncé.'),
        ('Colette', '2025', 'Salle de bain installée par HCI, nous sommes très contents du rendu final. Très bon suivi de coordination.'),
        ('Daniel', '2025', 'Entreprise sérieuse aussi bien sur les délais que sur la prestation fournie. Pas un seul défaut de prise de cote.'),
        ('Jean-Robert', '2024', 'Plans d’implantation bien pensés, meubles et appareils ménagers de qualité, installation impeccable.')]


def gal(items):
    return '<div class="gal">' + ''.join(f'<figure class="rv" data-c="{c}" style="--d:{(i % 3) * .07}s"><img src="{PH}{k}.webp" alt="{t}" loading="lazy"><figcaption><span class="micro">{c}</span>{t}</figcaption></figure>' for i, (k, c, t) in enumerate(items)) + '</div>'


def avis():
    return '<div class="avis">' + ''.join(f'<blockquote class="rv"><p>« {t} »</p><cite class="micro mute">{n} · avis Google · {d}</cite></blockquote>' for n, d, t in AVIS) + '</div>'


def service(file, title, desc, crumb, h1, lead, img, img2, intro_h, intro_p, checks, cats, faqs, more=''):
    items = [g for g in GAL if g[1] in cats][:6]
    extra = f'<div class="row rv" style="display:flex;gap:10px;flex-wrap:wrap;margin-top:2.2rem">{pill("Demander un devis", "contact.html", "blue")}{pill(TEL, TELH, "ghost")}</div>'
    cl = ''.join(f'<li><span><b>{a}</b> {b}</span></li>' for a, b in checks)
    return head(title, desc, file) + pagehead(crumb, h1, lead, img, img2, extra) + f'''
<section class="sec"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Notre savoir-faire</span><h2 class="sp">{intro_h}</h2><p class="lead rv" style="margin-top:1.4rem">{intro_p}</p></div><ul class="checks rv">{cl}</ul></div></section>{more}
<section class="sec" style="padding-top:0"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.2rem">Réalisations</span><h2 class="sp" style="margin-bottom:clamp(2rem,5vw,3.4rem)">Posées <em>chez nos clients</em></h2>{gal(items)}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Questions fréquentes</span><h2 class="sp">On vous <em>répond</em></h2></div><div class="rv">{faq(faqs)}</div></div></section>''' + cta() + foot()


FAQ_DEVIS = ('Le devis est-il gratuit ?', f'Oui. Appelez le {TEL}, écrivez-nous ou passez au showroom : nous étudions votre projet avec vous.')
FAQ_SALON = ('Où vous rencontrer ?', 'Au showroom de Châtillon-sur-Chalaronne, du lundi au vendredi, et sur les salons de l’habitat de la région.')
FAQ_AZ = ('Qui s’occupe de mon projet ?', 'Une même équipe, de la conception à la pose : plans, choix des matériaux, coordination des artisans et finitions.')


def pages():
    P = {}
    hero_tiles = [('t1', 'cuisine-noyer'), ('t2', 'salle-de-bain'), ('t3', 'cuisine-ilot'), ('t4', 'bibliotheque'), ('t5', 'cuisine-blanche'), ('t6', 'ilot-gris'), ('t7', 'cuisine-plan-beton')]
    ht = ''.join(f'<figure class="tile {c}"><div class="fl"><div class="in"><img src="{PH}{f}.webp" alt=""></div></div></figure>' for c, f in hero_tiles)
    stack = ''.join(tile(f'{PH}{f}.webp') for f in ['showroom', 'cuisine-ilot', 'cuisine-bois-clair', 'cuisine-noyer', 'salle-de-bain', 'bibliotheque', 'cuisine-blanche', 'cuisine-plan-beton'])
    wall_imgs = ['cuisine-noyer', 'salle-de-bain', 'cuisine-ilot', 'bibliotheque', 'cuisine-bois-clair', 'ilot-gris', 'cuisine-blanche', 'cuisine-grise', 'cuisine-plan-beton', 'cuisine-gris-bois', 'salle-a-manger', 'showroom']
    wall = ''.join(tile(f'{PH}{wall_imgs[i % len(wall_imgs)]}.webp') for i in range(54))
    items = [('cuisines.html', '01', 'Cuisines sur mesure', 'Élégantes et fonctionnelles, pensées pour votre quotidien.', 'cuisine-noyer'),
             ('amenagement.html', '02', 'Salles de bain', 'Modernes et raffinées, pour votre confort de tous les jours.', 'salle-de-bain'),
             ('amenagement.html#dressing', '03', 'Dressings et bibliothèques', 'Des rangements personnalisés, organisés et design.', 'bibliotheque'),
             ('amenagement.html#renovation', '04', 'Rénovation complète', 'De la conception aux finitions, nous coordonnons chaque étape.', 'cuisine-gris-bois')]
    pl = ''.join(f'<a href="{h}"><span class="micro mute">{n}</span><span class="nm">{t}</span><span class="d">{d}<b>Sur mesure</b></span></a>' for h, n, t, d, _ in items)
    prev = ''.join(tile(f'{PH}{it[4]}.webp', 'on' if i == 0 else '') for i, it in enumerate(items))
    track = ''.join(f'<figure class="tile"><img src="{PH}{f}.webp" alt="{l}" loading="lazy"><span class="tag">{l}</span></figure>' for f, l in [('cuisine-ilot', 'Cuisine en U'), ('salle-de-bain', 'Salle de bain'), ('cuisine-noyer', 'Cuisine ouverte'), ('bibliotheque', 'Bibliothèque'), ('ilot-gris', 'Îlot'), ('cuisine-blanche', 'Cuisine blanche')])
    steps = [('Rencontre', 'Au showroom ou sur un salon de l’habitat : vos envies, votre espace, votre budget.'),
             ('Plans et devis', 'Nous dessinons votre projet. Le devis est gratuit.'),
             ('Coordination', 'Menuisiers, plombiers, électriciens, carreleurs : nous organisons le chantier.'),
             ('Pose et finitions', 'Nos poseurs installent, nous suivons jusqu’au bout.')]
    st = ''.join(f'<div class="stp"><div class="n">{i + 1}</div><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(steps))
    mq = ''.join(f'<span>{x}</span>' for x in ['Cuisines', 'Salles de bain', 'Dressings', 'Bibliothèques', 'Rénovation', 'Sur mesure'] * 2)

    P['index.html'] = head('Habitat Concept Intérieur — Cuisiniste à Châtillon-sur-Chalaronne (Ain)', 'Habitat Concept Intérieur (HCI) à Châtillon-sur-Chalaronne : cuisines sur mesure, salles de bain, dressings et rénovation intérieure. Showroom, devis gratuit. 04 74 47 19 76.', 'index.html') + f'''
<section class="hero">
<div class="cap micro c1"><b>Cuisine</b>bain · dressing</div>
<div class="cap micro c2"><b>Sur mesure</b>de la conception à la pose</div>
<div class="cap micro c3"><b>Showroom</b>à Châtillon-sur-Chalaronne</div>
<div class="go">{pill('Devis gratuit', 'contact.html')}</div>
{ht}
<p class="para">Des intérieurs élégants, fonctionnels et conçus sur mesure.</p>
<h1 class="word">HCI CUISINES</h1>
<div class="scrollhint micro"><i></i>Défiler</div>
</section>

<div class="mq" aria-hidden="true"><div>{mq}</div></div>

<section class="sec"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.4rem">Votre cuisiniste à Châtillon</span><h2 class="sp">Donnez vie à <em>votre intérieur</em></h2>
<p class="lead rv" style="margin:1.4rem 0 2rem">De la cuisine sur mesure à la rénovation complète, chaque projet est pensé selon vos besoins et votre mode de vie.</p>
<ul class="checks rv" style="margin-bottom:2rem"><li><span><b>Une même équipe</b>, de la conception à la pose.</span></li><li><span><b>Un showroom</b> pour voir et toucher les matériaux.</span></li><li><span><b>Devis gratuit</b>, au {TEL}.</span></li></ul>{pill('Voir nos réalisations', 'realisations.html', 'blue')}</div>{tile(PH + 'cuisine-noyer.webp', '', par=8, alt='Cuisine ouverte avec îlot')}</div></section>

<section class="story"><span class="micro mute m3">Le savoir-faire</span>
<h2><span class="w">L’excellence</span> <span class="w">au</span> <span class="w">cœur</span> <span class="w">de</span> <span class="w">chaque</span> <span class="w"><em>réalisation</em></span></h2>
<div class="stack">{stack}</div>
<p class="micro mute m1">Qualité, savoir-faire, attention aux détails.</p><span class="micro mute m2">Finitions soignées</span></section>

<section class="wall"><div class="grid">{wall}</div><div class="mid"><span class="micro mute">Chez nos clients</span><h2>Nos <em>réalisations</em></h2>{pill('Voir les réalisations', 'realisations.html', 'blue')}</div></section>

<section class="sec" id="services"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Nos services</span><h2 class="sp" style="margin-bottom:clamp(2rem,5vw,4rem)">Quel est <em>votre projet ?</em></h2>
<div class="plist">{pl}</div></div><div class="prev">{prev}</div></section>

<section class="hz"><div class="pin"><div class="wrap top2"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Réalisations</span><h2>Pensées pour <em>votre quotidien</em></h2></div>{pill('Toutes les réalisations', 'realisations.html')}</div>
<div class="track">{track}</div></div></section>

<section class="sec"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Ils nous ont confié leur projet</span><h2 class="sp" style="margin-bottom:clamp(2rem,5vw,3.4rem)">Ce qu’en disent <em>nos clients</em></h2>{avis()}
<p class="note" style="margin-top:1.4rem">Extraits d’avis Google publiés, relevés le 13/11/2026.</p></div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Votre projet</span><h2 class="sp">Du premier plan <em>à la pose</em></h2><div class="steps">{st}</div></div></section>
{cta()}''' + foot()

    dressing = f'''
<section class="sec" id="dressing" style="padding-top:0"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Dressings et bibliothèques</span><h2 class="sp">Chaque centimètre <em>compte</em></h2>
<p class="lead rv" style="margin-top:1.4rem">Un dressing personnalisé, une bibliothèque murale, des rangements assortis : conçus pour optimiser votre espace et simplifier votre quotidien.</p></div>{tile(PH + 'bibliotheque.webp', '', par=8, alt='Bibliothèque murale sur mesure')}</div></section>
<section class="sec" id="renovation" style="padding-top:0"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Rénovation complète</span><h2 class="sp">Repensez <em>votre intérieur</em></h2>
<p class="lead rv" style="margin-top:1.4rem">Nous vous accompagnons dans la transformation complète de votre habitat. De la conception aux finitions, nous coordonnons chaque étape pour un résultat harmonieux.</p></div>{tile(PH + 'cuisine-gris-bois.webp', '', par=8, alt='Cuisine rénovée, gris et bois')}</div></section>'''

    P['cuisines.html'] = service('cuisines.html', 'Cuisines sur mesure à Châtillon-sur-Chalaronne — Habitat Concept Intérieur', 'Cuisines sur mesure, modernes et fonctionnelles : conception, plans, électroménager et pose. Showroom à Châtillon-sur-Chalaronne (Ain). Devis gratuit.',
        'Cuisines', 'Une cuisine <em>pensée pour vous</em>', 'Modernes et fonctionnelles, adaptées à vos habitudes de vie.', PH + 'cuisine-ilot.webp', PH + 'cuisine-blanche.webp',
        'Un lieu <em>où il fait bon vivre</em>', 'Chaque détail est étudié pour optimiser l’espace, améliorer le confort et créer un lieu convivial.',
        [('Conception', 'sur plans, selon votre espace et votre style.'), ('Matériaux', 'soigneusement sélectionnés, élégants et durables.'), ('Électroménager', 'intégré à votre projet.'), ('Pose', 'par nos poseurs, avec un suivi après-vente.')], ['Cuisines'],
        [FAQ_AZ, ('Pouvez-vous refaire toute la pièce ?', 'Oui : nous coordonnons aussi l’électricité, la plomberie et les finitions autour de votre cuisine.'), FAQ_SALON, FAQ_DEVIS])

    P['amenagement.html'] = service('amenagement.html', 'Salles de bain, dressings et rénovation — Habitat Concept Intérieur', 'Salles de bain modernes, dressings et bibliothèques sur mesure, rénovation intérieure complète. Habitat Concept Intérieur, Châtillon-sur-Chalaronne (Ain).',
        'Bain & dressing', 'Un espace <em>de bien-être</em>', 'Salles de bain, dressings, bibliothèques : des aménagements harmonieux, du sol au plafond.', PH + 'salle-de-bain.webp', PH + 'bibliotheque.webp',
        'Élégant <em>et pratique</em>', 'Nous créons des aménagements qui associent design contemporain, praticité et matériaux de qualité.',
        [('Salles de bain', 'douche à l’italienne, meubles vasques, faïence.'), ('Coordination', 'plombiers, carreleurs, poseurs de meubles.'), ('Dressings', 'et rangements sur mesure.'), ('Bibliothèques', 'murales, conçues pour votre pièce.')], ['Bain', 'Rangements'],
        [FAQ_AZ, ('Gérez-vous plombier et carreleur ?', 'Oui : nous coordonnons tous les artisans de votre salle de bain, et le planning suit l’avancée des travaux.'), FAQ_SALON, FAQ_DEVIS], dressing)

    P['realisations.html'] = head('Réalisations — Habitat Concept Intérieur, Châtillon-sur-Chalaronne', 'Cuisines, salles de bain, bibliothèques : quelques réalisations d’Habitat Concept Intérieur dans l’Ain et la région.', 'realisations.html') + pagehead('Réalisations', 'Nos <em>réalisations</em>', 'Cuisines, salles de bain et rangements posés chez nos clients.', PH + 'cuisine-noyer.webp', PH + 'cuisine-bois-clair.webp') + f'''
<section class="sec"><div class="wrap"><div class="flt" data-t=".gal figure"><button class="on" data-f="*">Tout</button><button data-f="Cuisines">Cuisines</button><button data-f="Bain">Salles de bain</button><button data-f="Rangements">Rangements</button><button data-f="Showroom">Showroom</button></div>{gal(GAL)}<p class="note" style="margin-top:2rem">Photos publiées par Habitat Concept Intérieur sur sa fiche Google.</p></div></section>''' + cta() + foot()

    P['contact.html'] = head('Contact et devis gratuit — Habitat Concept Intérieur', f'Devis gratuit pour votre cuisine, salle de bain ou dressing : {TEL}, {MAIL}. Showroom {ADR[0]}, {ADR[1]}.', 'contact.html') + pagehead('Contact', 'Parlons de <em>votre projet</em>', 'Cuisine, salle de bain, dressing ou rénovation : appelez-nous, écrivez-nous ou passez au showroom.', PH + 'showroom.webp') + f'''
<section class="sec" id="contact"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Coordonnées</span><h2 class="sp">Un appel <em>suffit</em></h2>
<div class="contactline rv" style="margin-top:2rem"><a href="{TELH}">{TEL}</a></div>
<p class="lead rv" style="margin-top:1.6rem"><a href="mailto:{MAIL}">{MAIL}</a><br>{ADR[0]}<br>{ADR[1]}</p>
<div class="hor rv"><span><b>Lundi au vendredi</b> : 9 h – 17 h</span><span>Samedi et dimanche : fermé</span><span class="micro">Horaires à confirmer avec l’entreprise</span></div></div>
<form class="f calc rv"><div class="r2"><div class="fld"><label for="n">Nom</label><input id="n" required></div><div class="fld"><label for="t">Téléphone</label><input id="t" type="tel" required></div></div>
<div class="fld"><label for="e">E-mail</label><input id="e" type="email"></div>
<div class="r2"><div class="fld"><label for="p">Projet</label><select id="p"><option>Cuisine</option><option>Salle de bain</option><option>Dressing ou bibliothèque</option><option>Rénovation complète</option><option>Autre</option></select></div><div class="fld"><label for="v">Commune</label><input id="v"></div></div>
<div class="fld"><label for="m">Votre projet en quelques mots</label><textarea id="m" rows="4" placeholder="Dimensions, style, neuf ou rénovation…"></textarea></div>
<button class="pill blue" type="submit" style="justify-self:start"><span class="r"><span>Envoyer</span><span>Envoyer</span></span><b>↗</b></button><div class="ok">Merci ! (Maquette : aucun message n’est envoyé.)</div></form></div></section>''' + foot()
    return P


for k, v in pages().items():
    open(os.path.join(OUT, k), 'w', encoding='utf-8').write(v)
print('ok')
