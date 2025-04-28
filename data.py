disease_map = {
    0: 'apple_apple_scab',
    1: 'apple_black_rot',
    2: 'apple_cedar_rust',
    3: 'apple_healthy',
    4: 'blueberry_healthy',
    5: 'cherry_powdery_mildew',
    6: 'cherry_healthy',
    7: 'corn_grey_leaf_spot',
    8: 'corn_common_rust',
    9: 'corn_northern_leaf_blight',
    10: 'corn_healthy',
    11: 'grape_black_rot',
    12: 'grape_black_measles',
    13: 'grape_leaf_blight',
    14: 'grape_healthy',
    15: 'orange_citrus_greening',
    16: 'peach_bacterial_spot',
    17: 'peach_healthy',
    18: 'bell_pepper_bacterial_spot',
    19: 'bell_pepper_healthy',
    20: 'potato_early_blight',
    21: 'potato_late_blight',
    22: 'potato_healthy',
    23: 'raspberry_healthy',
    24: 'rice_brown_spot',
    25: 'rice_hispa',
    26: 'rice_leaf_blast',
    27: 'rice_healthy',
    28: 'soybean_healthy',
    29: 'squash_powdery_mildew',
    30: 'strawberry_leaf_scorch',
    31: 'strawberry_healthy',
    32: 'tomato_bacterial_spot',
    33: 'tomato_early_blight',
    34: 'tomato_late_blight',
    35: 'tomato_leaf_mold',
    36: 'tomato_septoria_leaf_spot',
    37: 'tomato_spider_mites',
    38: 'tomato_target_spot',
    39: 'tomato_yellow_leaf_curl_virus',
    40: 'tomato_mosaic_virus',
    41: 'tomato_healthy',
}


details_map = {
    'apple_apple_scab': [
        'A serious disease of apples and ornamental crabapples, apple scab (Venturia inaequalis) attacks both leaves and fruit. The fungal disease forms pale yellow or olive-green spots on the upper surface of leaves. Dark, velvety spots may appear on the lower surface. Severely infected leaves become twisted and puckered and may drop early in the summer.',
        'Symptoms on fruit are similar to those found on leaves. Scabby spots are sunken and tan and may have velvety spores in the center. As these spots mature, they become larger and turn brown and corky. Infected fruit becomes distorted and may crack allowing entry of secondary organisms. Severely affected fruit may drop, especially when young.',
        'https://www.planetnatural.com/pest-problem-solver/plant-disease/apple-scab'],
    'apple_black_rot': [
        'Black rot is occasionally a problem on Minnesota apple trees. This fungal disease causes leaf spot, fruit rot and cankers on branches. Trees are more likely to be infected if they are: Not fully hardy in Minnesota, Infected with fire blight or Stressed by environmental factors like drought.',
        'Large brown rotten areas can form anywhere on the fruit but are most common on the blossom end. Brown to black concentric rings can often be seen on larger infections. The flesh of the apple is brown but remains firm. Infected leaves develop "frog-eye leaf spot". These are circular spots with purplish or reddish edges and light tan interiors.',
        'https://extension.umn.edu/plant-diseases/black-rot-apple'],
    'apple_cedar_rust': [
        'Cedar apple rust (Gymnosporangium juniperi-virginianae) is a fungal disease that requires juniper plants to complete its complicated two year life-cycle. Spores overwinter as a reddish-brown gall on young twigs of various juniper species. In early spring, during wet weather, these galls swell and bright orange masses of spores are blown by the wind where they infect susceptible apple and crab-apple trees. The spores that develop on these trees will only infect junipers the following year. From year to year, the disease must pass from junipers to apples to junipers again; it cannot spread between apple trees.',
        'On apple and crab-apple trees, look for pale yellow pinhead sized spots on the upper surface of the leaves shortly after bloom. These gradually enlarge to bright orange-yellow spots which make the disease easy to identify. Orange spots may develop on the fruit as well. Heavily infected leaves may drop prematurely.',
        'https://www.planetnatural.com/pest-problem-solver/plant-disease/cedar-apple-rust'],
    'apple_healthy': [
        'Your crops are healthy. You took good care of it.',
        'Healthy Crops',
        'Just take care of it as you usually do.'],
    'blueberry_healthy': [
        'Your crops are healthy. You took good care of it.',
        'Healthy Crops',
        'Just take care of it as you usually do.'],
    'cherry_powdery_mildew': [
        'Powdery mildew of sweet and sour cherry is caused by Podosphaera clandestina, an obligate biotrophic fungus. Mid- and late-season sweet cherry (Prunus avium) cultivars are commonly affected, rendering them unmarketable due to the covering of white fungal growth on the cherry surface. Season long disease control of both leaves and fruit is critical to minimize overall disease pressure in the orchard and consequently to protect developing fruit from accumulating spores on their surfaces.',
        'Initial symptoms, often occurring 7 to 10 days after the onset of the first irrigation, are light roughly-circular, powdery looking patches on young, susceptible leaves (newly unfolded, and light green expanding leaves). Older leaves develop an age-related (ontogenic) resistance to powdery mildew and are naturally more resistant to infection than younger leaves. Look for early leaf infections on root suckers, the interior of the canopy or the crotch of the tree where humidity is high.',
        'http://treefruit.wsu.edu/crop-protection/disease-management/cherry-powdery-mildew'],
    'Cherry_healthy': [
        'Your crops are healthy. You took good care of it.',
        'Healthy Crops',
        'Just take care of it as you usually do.'],
    'corn_grey_leaf_spot': [
        'Gray leaf spot (GLS) is a common fungal disease in the United States caused by the pathogen Cercospora zeae-maydis in corn. Disease development is favored by warm temperatures, 80°F or 27 °C; and high humidity, relative humidity of 90% or higher for 12 hours or more. Cercospora zeae-maydis overwinters in corn residue, allowing inoculum to build up from year to year in fields. Cropping systems with reduced- or no-till and/or continuous corn are at higher risk for gray leaf spot outbreaks.',
        'Gray leaf spot lesions begin as small necrotic pinpoints with chlorotic halos, these are more visible when leaves are backlit. Coloration of initial lesions can range from tan to brown before sporulation begins. Because early lesions are ambiguous, they are easily confused with other foliar diseases such as anthracnose leaf blight, eyespot, or common rust. As infection progresses, lesions begin to take on a more distinct shape. Lesion expansion is limited by parallel leaf veins, resulting in the blocky shaped “spots”. As sporulation commences, the lesions take on a more gray coloration.',
        'https://www.pioneer.com/us/agronomy/gray_leaf_spot_cropfocus.html'],
    'corn_common_rust': [
        'Common rust is caused by the fungus Puccinia sorghi. Late occurring infections have limited impact on yield. The fungus overwinters on plants in southern states and airborne spores are wind-blown to northern states during the growing season. Disease development is favored by cool, moist weather (60 – 70◦ F).',
        'Symptoms of common rust often appear after silking. Small, round to elongate brown pustules form on both leaf surfaces and other above ground parts of the plant. As the pustules mature they become brown to black. If disease is severe, the leaves may yellow and die early.',
        'https://fieldcrops.cals.cornell.edu/corn/diseases-corn/common-rust'],
    'corn_northern_leaf_blight': [
        'Northern corn leaf blight caused by the fungus Exerohilum turcicum is a common leaf blight. If lesions begin early (before silking), crop loss can result. Late infections may have less of an impact on yield. Northern corn leaf blight is favored by wet humid cool weather typically found later in the growing season. Spores of the fungus that causes this disease can be transported by wind long distances from infected fields. Spread within and between fields locally also relies on wind blown spores.',
        'The tan lesions of northern corn leaf blight are slender and oblong tapering at the ends ranging in size between 1 to 6 inches. Lesions run parallel to the leaf margins beginning on the lower leaves and moving up the plant. They may coalesce and cover the enter leaf. Spores are produced on the underside of the leaf below the lesions giving the appearance of a dusty green fuzz.',
        'https://fieldcrops.cals.cornell.edu/corn/diseases-corn/northern-corn-leaf-blight'],
    'corn_healthy': [
        'Your crops are healthy. You took good care of it.',
        'Healthy Crops',
        'Just take care of it as you usually do.'],
    'grape_black_rot': [
        'Black rot is one of the most damaging diseases of grapes. The disease is caused by the fungus Guignardia bidwellii. The fungus can infect the leaves, shoots, berries, tendrils, rachises and cluster stems (peduncles) of grapes. If the disease is not managed early in the season, the impact on grape clusters can be devastating, resulting in complete crop losses.',
        'Disease development is favored by warm and humid weather. Symptoms of black rot first appear as small yellow spots on leaves. Enlarged spots (lesions) have a dark brownish-red border with tan to dark brown centers. As the infection develops, tiny black dots appear in the lesion, usually in a ring pattern near the border of the lesion. These dots are fungal structures (pycnidia), which contain thousands of spores (conidia) that can infect new tissue. New infections can occur in less than 10 hours at temperatures between 60 to 85 degrees Fahrenheit.',
        'https://ohioline.osu.edu/factsheet/plpath-fru-24'],
    'grape_black_measles': [
        'Grapevine measles, also called esca, black measles or Spanish measles, has long plagued grape growers with its cryptic expression of symptoms and, for a long time, a lack of identifiable causal organism(s). The name "measles" refers to the superficial spots found on the fruit. During the season, the spots may coalesce over the skin surface, making berries black in appearance. Spotting can develop anytime between fruit set and a few days prior to harvest.',
        'Leaf symptoms are characterized by a "tiger stripe" pattern when infections are severe from year to year. Mild infections can produce leaf symptoms that can be confused with other diseases or nutritional deficiencies. White cultivars will display areas of chlorosis followed by necrosis, while red cultivars are characterized by red areas followed by necrosis. Early spring symptoms include shoot tip dieback, leaf discoloration and complete defoliation in severe cases.',
        'https://grapes.extension.org/grapevine-measles'],
    'grape_leaf_blight': [
        'Common in tropical and subtropical grapes. The disease appear late in the season. Cynthiana and Cabernet Sauvignon are susceptible to this pathogen.',
        'On leaf surface we will see lesions which are irregularly shaped (2 to 25 mm in diameter). Initially lesions are dull red to brown in color turn black later. If disease is severe this lesions may coalesce. On berries we can see symptom similar to black rot but the entire clusters will collapse.',
        'https://plantvillage.psu.edu/topics/grape/infos'],
    'grape_healthy': [
        'Your crops are healthy. You took good care of it.',
        'Healthy Crops',
        'Just take care of it as you usually do.'],
    'orange_citrus_greening': [
        'Huanglongbing (HLB) or citrus greening is the most severe citrus disease, currently devastating the citrus industry worldwide. The presumed causal bacterial agent Candidatus Liberibacter spp. affects tree health as well as fruit development, ripening and quality of citrus fruits and juice. Fruit from infected orange trees can be either symptomatic or asymptomatic. Symptomatic oranges are small, asymmetrical and greener than healthy fruit. Furthermore, symptomatic oranges show higher titratable acidity and lower soluble solids, solids/acids ratio, total sugars, and malic acid levels.',
        'In the early stages of the disease, it is difficult to make a clear diagnosis. McCollum and Baldwin (2017) noted that HLB symptoms are more apparent during cooler seasons, more so than in warmer months. It is uncertain how long a tree can be infected before showing the symptoms of the disease but, when it eventually becomes symptomatic, symptoms appear on different parts of the tree. Infected trees generally develop some canopy thinning, with twig dieback and discolored leaves, which appear in contrast to the other healthy or symptomless parts of the tree.',
        'https://www.frontiersin.org/articles/10.3389/fpls.2018.01976/full'],
     'peach_bacterial_spot': [
        'Bacterial spot affects peaches, nectarines, apricots, plums, prunes and cherries. The disease is widespread throughout all fruit growing states east of the Rocky Mountains. Bacterial spot can affect leaves, twigs, and fruit. Severe infection results in reduced fruit quality and yield...',
        'Small (1/25 to 1/5 inch) spots form in the leaves... Badly infected leaves may turn yellow and drop early...',
        'https://ohioline.osu.edu/factsheet/plpath-fru-38'
    ],
    'peach_healthy': [
        'Your crops are healthy. You took good care of it.',
        'Healthy Crops',
        'Just take care of it as you usually do.'
    ],
    'bell_pepper_bacterial_spot': [
        'Bacterial leaf spot, caused by Xanthomonas campestris pv. vesicatoria, is the most common and destructive disease for peppers in the eastern United States...',
        'Disease symptoms can appear throughout the above-ground portion of the plant... Over time, these spots can dry up in less humid weather...',
        'https://extension.wvu.edu/lawn-gardening-pests/plant-disease/fruit-vegetable-diseases/bacterial-leaf-spot-of-pepper'
    ],
    'bell_pepper_healthy': [
        'Your crops are healthy. You took good care of it.',
        'Healthy Crops',
        'Just take care of it as you usually do.'
    ],
    'potato_early_blight': [
        'Common on tomato and potato plants, early blight is caused by the fungus Alternaria solani...',
        'Early blight overwinters on infected plant tissue and is spread by splashing rain, irrigation, insects and garden tools...',
        'https://www.planetnatural.com/pest-problem-solver/plant-disease/early-blight'
    ],
    'potato_late_blight': [
        'Late blight (Phytophthora infestans) fungus is in the same genus as the fungus causing pink rot...',
        'Late blight will first appear as water-soaked spots... Under continuously wet conditions, the disease progresses rapidly...',
        'https://cropwatch.unl.edu/potato/late_blights'
    ],
    'potato_healthy': [
        'Your crops are healthy. You took good care of it.',
        'Healthy Crops',
        'Just take care of it as you usually do.'
    ],
    'raspberry_healthy': [
        'Your crops are healthy. You took good care of it.',
        'Healthy Crops',
        'Just take care of it as you usually do.'
    ],
    'rice_brown_spot': [
        'Brown Spot is called as sesame leaf spot or Helminthosporiose or fungal blight...',
        'The disease appears first as minute brown dots... Infection also occurs on panicle, neck with brown colour appearance...',
        'http://www.agritech.tnau.ac.in/expert_system/paddy/cpdisbrownspot.html'
    ],
    'rice_hispa': [
        'The mining of the grubs will be clearly seen on the leaves... Rice field appears burnt when severely infested.',
        'The grub mines into the leaf blade and feed on the green tissue between the veins...',
        'http://www.agritech.tnau.ac.in/expert_system/paddy/cppests_ricehispa.html'
    ],
    'rice_leaf_blast': [
        'Blast, also called rotten neck, is one of the most destructive diseases of Missouri rice...',
        'Blast symptoms can occur on leaves, leaf collars, nodes and panicles... Lesions on leaf sheaths resemble those on leaves.',
        'https://extension.missouri.edu/publications/mp645'
    ],
    'rice_healthy': [
        'Your crops are healthy. You took good care of it.',
        'Healthy Crops',
        'Just take care of it as you usually do.'
    ],
    'soybean_healthy': [
        'Your crops are healthy. You took good care of it.',
        'Healthy Crops',
        'Just take care of it as you usually do.'
    ],
    'squash_powdery_mildew': [
        'Powdery mildew, mainly caused by the fungus Podosphaera xanthii, infects all cucurbits, including muskmelons, squash, cucumbers, gourds, watermelons and pumpkins. In severe cases, powdery mildew can cause premature death of leaves, and reduce yield and fruit quality.',
        'The first sign of powdery mildew is pale yellow leaf spots. White powdery spots can form on both upper and lower leaf surfaces, and quickly expand into large blotches. The large blotches can cover entire leaf, petiole and stem surfaces. When powdery mildew infects the majority of the foliage, the plant weakens and the fruit ripens prematurely.',
        'https://extension.umn.edu/diseases/powdery-mildew-cucurbits'],
    'strawberry_leaf_scorch': [
        'In addition to leaves, leaf scorch (Diplocarpon earlianum) can infect petioles, runners, fruit stalks and berry caps. If unchecked, plants can be significantly weakened reducing the growth of all plant parts. Severely infected plants are weakened and can die from other stresses such as drought or extreme temperatures.',
        'Dark purple, angular to round spots appear on the upper surface of the leaf. As the disease progresses the tissues around these spots turn reddish or purple. In severe cases, the infected area dries to a tan color and the leaf curls upward looking scorched. Lesions remain reddish purple and do not turn tan or gray in the center.',
        'https://extension.umn.edu/fruit/growing-strawberries-home-garden#gray-mold%2C-leaf-blight%2C-leaf-scorch-and-leaf-spot--1008160'],
    'strawberry_healthy': [
        'Your crops are healthy. You took good care of it.',
        'Healthy Crops',
        'Just take care of it as you usually do.'],
    'tomato_bacterial_spot': [
        'Bacterial spot can be a devastating disease when the weather is warm and humid. The disease can affect all above-ground parts of tomato and pepper plants: stems, petioles, leaves, and fruits. Fruit spots commonly result in unmarketable fruit, not only for fresh market but also for processing because the spots make the fruit difficult to peel.',
        'Tomato leaves have small (<1/8 inch), brown, circular spots surrounded by a yellow halo. The center of the leaf spots often falls out resulting in small holes. Small, brown, circular spots may also occur on stems and the fruit calyx. Fruit spots are ¼ inch, slightly raised, brown and scabby. Tomato fruit often have a waxy white halo surrounding the fruit spot.',
        'https://extension.umn.edu/diseases/bacterial-spot-tomato-and-pepper'],
    'tomato_early_blight': [
        'Early blight is one of the most common tomato diseases, occurring nearly every season wherever tomatoes are grown. It affects leaves, fruits and stems and can be severely yield limiting when susceptible cultivars are used and weather is favorable. Severe defoliation can occur and result in sunscald on the fruit. Early blight is common in both field and high tunnel tomato production in Minnesota.',
        'Initially, small dark spots form on older foliage near the ground. Leaf spots are round, brown and can grow up to half inch in diameter. Larger spots have target-like concentric rings. The tissue around spots often turns yellow. Severely infected leaves turn brown and fall off, or dead, dried leaves may cling to the stem.',
        'https://extension.umn.edu/diseases/early-blight-tomato'],
    'tomato_late_blight': [
        'Late blight is a potentially devastating disease of tomato and potato, infecting leaves, stems and fruits of tomato plants. The disease spreads quickly in fields and can result in total crop failure if untreated. Late blight of potato was responsible for the Irish potato famine of the late 1840s.',
        'Leaves have large, dark brown blotches with a green gray edge; not confined by major leaf veins. Infections progress through leaflets and petioles, resulting in large sections of dry brown foliage. Stem infections are firm and dark brown with a rounded edge.',
        'https://extension.umn.edu/diseases/late-blight'],
    'tomato_leaf_mold': [
        'Leaf mold is not normally a problem in field-grown tomatoes in northern climates. It can cause losses in tomatoes grown in greenhouses or high tunnels due to the higher humidity found in these environments. Foliage is often the only part of the plant infected and will cause infected leaves to wither and die, indirectly affecting yield. In severe cases, blossoms and fruit can also be infected, directly reducing yield.',
        'The oldest leaves are infected first. Pale greenish-yellow spots, usually less than 1/4 inch, with no definite margins, form on upper sides of leaves. Olive-green to brown velvety mold forms on the lower leaf surface below leaf spots. Leaf spots grow together and turn brown. Leaves wither and die but often remain attached to the plant.',
        'https://extension.umn.edu/diseases/leaf-mold-tomato'],
    'tomato_septoria_leaf_spot': [
        'Septoria leaf spot is a very common disease of tomatoes. It is caused by a fungus (Septoria lycopersici) and can affect tomatoes and other plants in the Solanaceae family, especially potatoes and eggplant, just about anywhere in the world. Although Septoria leaf spot is not necessarily fatal for your tomato plants, it spreads rapidly and can quickly defoliate and weaken the plants, rendering them unable to bear fruit to maturity.',
        'Septoria leaf spots start off somewhat circular and first appear on the undersides of older leaves, at the bottom of the plant. They are small, 1/16 to 1/8 inches (1.6 to 3.2 millimeters) in diameter, with a dark brown margin and lighter gray or tan centers. A yellow halo may surround the spot.',
        'https://www.thespruce.com/identifying-and-controlling-septoria-leaf-spot-of-tomato-1402974'],
    'tomato_spider_mites': [
        'Many species of the spider mite (family: Tetranychidae), so common in North America, attack both indoor and outdoor plants. They can be especially destructive in greenhouses. Spider mites are not true insects, but are classed as a type of arachnid, relatives of spiders, ticks and scorpions.',
        'Spider mites, almost too small to be seen, pass into our gardens without notice. No matter how few, each survives by sucking material from plant cells. Large infestations cause visible damage. Leaves first show patterns of tiny spots or stipplings. They may change color, curl and fall off. The mites activity is visible in the tight webs that are formed under leaves and along stems.',
        'https://www.planetnatural.com/pest-problem-solver/houseplant-pests/spider-mite-control'],
    'tomato_target_spot': [
        'Also known as early blight, target spot of tomato is a fungal disease that attacks a diverse assortment of plants, including papaya, peppers, snap beans, potatoes, cantaloupe, and squash as well as passion flower and certain ornamentals. Target spot on tomato fruit is difficult to control because the spores, which survive on plant refuse in the soil, are carried over from season to season.',
        'Target spot on tomato fruit is difficult to recognize in the early stages, as the disease resembles several other fungal diseases of tomatoes. However, as diseased tomatoes ripen and turn from green to red, the fruit displays circular spots with concentric, target-like rings and a velvety black, fungal lesions in the center. The "targets" become pitted and larger as the tomato matures.',
        'https://www.gardeningknowhow.com/edible/vegetables/tomato/target-spot-on-tomatoes.htm'],
    'tomato_yellow_leaf_curl_virus': [
        'Tomato yellow leaf curl virus is undoubtedly one of the most damaging pathogens of tomato, and it limits production of tomato in many tropical and subtropical areas of the world. It is also a problem in many countries that have a Mediterranean climate such as California. Thus, the spread of the virus throughout California must be considered as a serious potential threat to the tomato industry.',
        'Infected tomato plants initially show stunted and erect or upright plant growth; plants infected at an early stage of growth will show severe stunting. However, the most diagnostic symptoms are those in leaves.',
        'https://www2.ipm.ucanr.edu/agriculture/tomato/tomato-yellow-leaf-curl'],
    'tomato_mosaic_virus': [
        'Tomato mosaic virus (ToMV) and  Tobacco mosaic virus (TMV) are hard to distinguish. Tomato mosaic virus (ToMV) can cause yellowing and stunting of tomato plants resulting in loss of stand and reduced yield. ToMV may cause uneven ripening of fruit, further reducing yield.',
        'Mottled light and dark green on leaves. If plants are infected early, they may appear yellow and stunted overall. Leaves may be curled, malformed, or reduced in size. Spots of dead leaf tissue may become apparent with certain cultivars at warm temperatures. Fruits may ripen unevenly. Reduced fruit number and size.',
        'https://extension.umn.edu/diseases/tomato-mosaic-virus-and-tobacco-mosaic-virus'],
    'tomato_healthy': [
        'Your crops are healthy. You took good care of it.',
        'Healthy Crops',
        'Just take care of it as you usually do.']
    }