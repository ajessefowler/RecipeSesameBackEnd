from datetime import datetime
import enum
from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")

recipes =  [
    {
    "title": "Slow Cooker Chicken and Dumplings",
    "ingredients": [
      "4 skinless, boneless chicken breast halves ADVERTISEMENT",
      "2 tablespoons butter ADVERTISEMENT",
      "2 (10.75 ounce) cans condensed cream of chicken soup ADVERTISEMENT",
      "1 onion, finely diced ADVERTISEMENT",
      "2 (10 ounce) packages refrigerated biscuit dough, torn into pieces ADVERTISEMENT",
      "ADVERTISEMENT"
    ],
    "instructions": "Place the chicken, butter, soup, and onion in a slow cooker, and fill with enough water to cover.\nCover, and cook for 5 to 6 hours on High. About 30 minutes before serving, place the torn biscuit dough in the slow cooker. Cook until the dough is no longer raw in the center.\n",
    "picture_link": "55lznCYBbs2mT8BTx6BTkLhynGHzM.S"
  },
  {
    "title": "Awesome Slow Cooker Pot Roast",
    "ingredients": [
      "2 (10.75 ounce) cans condensed cream of mushroom soup ADVERTISEMENT",
      "1 (1 ounce) package dry onion soup mix ADVERTISEMENT",
      "1 1/4 cups water ADVERTISEMENT",
      "5 1/2 pounds pot roast ADVERTISEMENT",
      "ADVERTISEMENT"
    ],
    "instructions": "In a slow cooker, mix cream of mushroom soup, dry onion soup mix and water. Place pot roast in slow cooker and coat with soup mixture.\nCook on High setting for 3 to 4 hours, or on Low setting for 8 to 9 hours.\n",
    "picture_link": "QyrvGdGNMBA2lDdciY0FjKu.77MM0Oe"
  },
  {
    "title": "Brown Sugar Meatloaf",
    "ingredients": [
      "1/2 cup packed brown sugar ADVERTISEMENT",
      "1/2 cup ketchup ADVERTISEMENT",
      "1 1/2 pounds lean ground beef ADVERTISEMENT",
      "3/4 cup milk ADVERTISEMENT",
      "2 eggs ADVERTISEMENT",
      "1 1/2 teaspoons salt ADVERTISEMENT",
      "1/4 teaspoon ground black pepper ADVERTISEMENT",
      "1 small onion, chopped ADVERTISEMENT",
      "1/4 teaspoon ground ginger ADVERTISEMENT",
      "3/4 cup finely crushed saltine cracker crumbs ADVERTISEMENT",
      "ADVERTISEMENT"
    ],
    "instructions": "Preheat oven to 350 degrees F (175 degrees C). Lightly grease a 5x9 inch loaf pan.\nPress the brown sugar in the bottom of the prepared loaf pan and spread the ketchup over the sugar.\nIn a mixing bowl, mix thoroughly all remaining ingredients and shape into a loaf. Place on top of the ketchup.\nBake in preheated oven for 1 hour or until juices are clear.\n",
    "picture_link": "LVW1DI0vtlCrpAhNSEQysE9i/7rJG56"
  },
  {
    "title": "Best Chocolate Chip Cookies",
    "ingredients": [
      "1 cup butter, softened ADVERTISEMENT",
      "1 cup white sugar ADVERTISEMENT",
      "1 cup packed brown sugar ADVERTISEMENT",
      "2 eggs ADVERTISEMENT",
      "2 teaspoons vanilla extract ADVERTISEMENT",
      "3 cups all-purpose flour ADVERTISEMENT",
      "1 teaspoon baking soda ADVERTISEMENT",
      "2 teaspoons hot water ADVERTISEMENT",
      "1/2 teaspoon salt ADVERTISEMENT",
      "2 cups semisweet chocolate chips ADVERTISEMENT",
      "1 cup chopped walnuts ADVERTISEMENT",
      "ADVERTISEMENT"
    ],
    "instructions": "Preheat oven to 350 degrees F (175 degrees C).\nCream together the butter, white sugar, and brown sugar until smooth. Beat in the eggs one at a time, then stir in the vanilla. Dissolve baking soda in hot water. Add to batter along with salt. Stir in flour, chocolate chips, and nuts. Drop by large spoonfuls onto ungreased pans.\nBake for about 10 minutes in the preheated oven, or until edges are nicely browned.\n",
    "picture_link": "0SO5kdWOV94j6EfAVwMMYRM3yNN8eRi"
  },
  {
    "title": "Homemade Mac and Cheese Casserole",
    "ingredients": [
      "8 ounces whole wheat rotini pasta ADVERTISEMENT",
      "3 cups fresh broccoli florets ADVERTISEMENT",
      "1 medium onion, chopped ADVERTISEMENT",
      "3 cloves garlic, minced ADVERTISEMENT",
      "4 tablespoons butter, divided ADVERTISEMENT",
      "2 tablespoons all-purpose flour ADVERTISEMENT",
      "1/4 teaspoon salt ADVERTISEMENT",
      "1/8 teaspoon ground black pepper ADVERTISEMENT",
      "2 1/2 cups milk ADVERTISEMENT",
      "8 ounces Cheddar cheese, shredded ADVERTISEMENT",
      "4 ounces reduced-fat cream cheese, cubed and softened ADVERTISEMENT",
      "1/2 cup fine dry Italian-seasoned bread crumbs ADVERTISEMENT",
      "Reynolds Wrap\u00ae Non Stick Aluminum Foil ADVERTISEMENT",
      "ADVERTISEMENT"
    ],
    "instructions": "Preheat oven to 350 degrees F. Line a 2-quart casserole dish with Reynolds Wrap(R) Pan Lining Paper, parchment side up. No need to grease dish.\nCook the pasta in a large saucepan according to the package directions, adding the broccoli for the last 3 minutes of cooking. Drain. Return to the saucepan and set aside.\nCook the onion and garlic in 2 tablespoons hot butter in a large skillet 5 to 7 minutes or until tender. Stir in flour, salt, and black pepper. Add the milk all at once. Cook and stir over medium heat until slightly thickened and bubbly. Add cheddar cheese and cream cheese, stirring until melted. Pour cheese sauce over the pasta and broccoli and stir until well combined.\nMelt the remaining 2 tablespoons butter and mix with the bread crumbs in a small bowl. Transfer the pasta mixture to the prepared casserole dish. Top with the buttery bread crumbs.\nBake, uncovered, about 25 minutes or until bubbly and internal temperature is 165 degrees F. Let stand for 10 minutes before serving.\n",
    "picture_link": "YCnbhplMgiraW4rUXcybgSEZinSgljm"
  },
  {
    "title": "Banana Banana Bread",
    "ingredients": [
      "2 cups all-purpose flour ADVERTISEMENT",
      "1 teaspoon baking soda ADVERTISEMENT",
      "1/4 teaspoon salt ADVERTISEMENT",
      "1/2 cup butter ADVERTISEMENT",
      "3/4 cup brown sugar ADVERTISEMENT",
      "2 eggs, beaten ADVERTISEMENT",
      "2 1/3 cups mashed overripe bananas ADVERTISEMENT",
      "ADVERTISEMENT"
    ],
    "instructions": "Preheat oven to 350 degrees F (175 degrees C). Lightly grease a 9x5 inch loaf pan.\nIn a large bowl, combine flour, baking soda and salt. In a separate bowl, cream together butter and brown sugar. Stir in eggs and mashed bananas until well blended. Stir banana mixture into flour mixture; stir just to moisten. Pour batter into prepared loaf pan.\nBake in preheated oven for 60 to 65 minutes, until a toothpick inserted into center of the loaf comes out clean. Let bread cool in pan for 10 minutes, then turn out onto a wire rack.\n",
    "picture_link": "jRnWGDXDdyOg3rta4/HVAR2rD19XubC"
  },
  {
    "title": "Chef John's Fisherman's Pie",
    "ingredients": [
      "For potato crust: ADVERTISEMENT",
      "3 russet potatoes, peeled and cut into chunks ADVERTISEMENT",
      "3 tablespoons butter ADVERTISEMENT",
      "1 pinch freshly grated nutmeg ADVERTISEMENT",
      "salt and ground black pepper to taste ADVERTISEMENT",
      "1 pinch cayenne pepper, or to taste ADVERTISEMENT",
      "1/2 cup milk ADVERTISEMENT",
      "For the spinach: ADVERTISEMENT",
      "2 teaspoons olive oil ADVERTISEMENT",
      "12 ounces baby spinach leaves ADVERTISEMENT",
      "For the sauce: ADVERTISEMENT",
      "3 tablespoons butter ADVERTISEMENT",
      "3 tablespoons all-purpose flour ADVERTISEMENT",
      "2 cloves garlic, minced ADVERTISEMENT",
      "2 cups cold milk, divided ADVERTISEMENT",
      "2 teaspoons lemon zest ADVERTISEMENT",
      "For the rest: ADVERTISEMENT",
      "1 tablespoon butter ADVERTISEMENT",
      "salt and ground black pepper to taste ADVERTISEMENT",
      "1 pinch cayenne pepper, or to taste ADVERTISEMENT",
      "2 pounds boneless cod fillets ADVERTISEMENT",
      "1/2 lemon, juiced ADVERTISEMENT",
      "1 tablespoon chopped fresh chives for garnish ADVERTISEMENT",
      "ADVERTISEMENT"
    ],
    "instructions": "Bring a large saucepan of salted water and to a boil; add russet potatoes to boiling water and cook until very tender, about 20 minutes. Drain well. Mash in 3 tablespoons butter until thoroughly combined. Season with nutmeg, salt, black pepper, and cayenne pepper to taste. Mash 1/2 cup milk into potato mixture until smooth.\nDrizzle olive oil in a large Dutch oven over medium-high heat, add spinach, and season with a big pinch of salt. Cook, stirring occasionally, until spinach has wilted, about 1 minute. Transfer to a bowl lined with paper towels to wick away excess moisture.\nHeat 3 tablespoons butter and flour in a saucepan over medium heat; whisk mixture to a smooth paste. Cook, stirring constantly, until mixture has a nutty smell and is slightly browned, about 2 minutes. Add chopped garlic; whisk until fragrant, 10 to 20 seconds.\nWhisk 1 cup cold milk into flour mixture; cook until thickened. Whisk in remaining 1 cup milk and lemon zest. Bring white sauce to a gentle simmer, whisking constantly; season with salt. Turn heat to very low and keep sauce warm.\nPreheat oven to 375 degrees F (190 degrees C). Grease an 8x12-inch casserole dish with 1 tablespoon butter.\nSeason buttered pan with salt, black pepper, and cayenne pepper. Lay boneless cod fillets into the pan in a single layer. Season tops of fillets with more salt, black pepper, and cayenne pepper. Spread spinach evenly over fish and drizzle with lemon juice. Spoon white sauce over spinach; give casserole dish several taps and shakes to eliminate bubbles.\nDrop mashed potatoes by heaping spoonfuls over the casserole and spread smoothly to cover. Place dish onto a rimmed baking sheet to catch spills.\nBake in the preheated oven until bubbling, about 40 minutes. Turn on oven's broiler and broil until potato crust has a golden brown top, about 2 minutes. Fish should flake easily. Let stand 10 minutes before serving. Garnish with a sprinkle of chives.\n",
    "picture_link": "aUca10AaD8T2yYvcLOgH/UJlR5/OhOe"
  },
  {
    "title": "Mom's Zucchini Bread",
    "ingredients": [
      "3 cups all-purpose flour ADVERTISEMENT",
      "1 teaspoon salt ADVERTISEMENT",
      "1 teaspoon baking soda ADVERTISEMENT",
      "1 teaspoon baking powder ADVERTISEMENT",
      "1 tablespoon ground cinnamon ADVERTISEMENT",
      "3 eggs ADVERTISEMENT",
      "1 cup vegetable oil ADVERTISEMENT",
      "2 1/4 cups white sugar ADVERTISEMENT",
      "3 teaspoons vanilla extract ADVERTISEMENT",
      "2 cups grated zucchini ADVERTISEMENT",
      "1 cup chopped walnuts ADVERTISEMENT",
      "ADVERTISEMENT"
    ],
    "instructions": "Grease and flour two 8 x 4 inch pans. Preheat oven to 325 degrees F (165 degrees C).\nSift flour, salt, baking powder, soda, and cinnamon together in a bowl.\nBeat eggs, oil, vanilla, and sugar together in a large bowl. Add sifted ingredients to the creamed mixture, and beat well. Stir in zucchini and nuts until well combined. Pour batter into prepared pans.\nBake for 40 to 60 minutes, or until tester inserted in the center comes out clean. Cool in pan on rack for 20 minutes. Remove bread from pan, and completely cool.\n",
    "picture_link": "YdgEVyLVffZgh9NZPN3Eqj6MaX8KdzK"
  },
   {
    "title": "The Best Rolled Sugar Cookies",
    "ingredients": [
      "1 1/2 cups butter, softened ADVERTISEMENT",
      "2 cups white sugar ADVERTISEMENT",
      "4 eggs ADVERTISEMENT",
      "1 teaspoon vanilla extract ADVERTISEMENT",
      "5 cups all-purpose flour ADVERTISEMENT",
      "2 teaspoons baking powder ADVERTISEMENT",
      "1 teaspoon salt ADVERTISEMENT",
      "ADVERTISEMENT"
    ],
    "instructions": "In a large bowl, cream together butter and sugar until smooth. Beat in eggs and vanilla. Stir in the flour, baking powder, and salt. Cover, and chill dough for at least one hour (or overnight).\nPreheat oven to 400 degrees F (200 degrees C). Roll out dough on floured surface 1/4 to 1/2 inch thick. Cut into shapes with any cookie cutter. Place cookies 1 inch apart on ungreased cookie sheets.\nBake 6 to 8 minutes in preheated oven. Cool completely.\n",
    "picture_link": "UrgvDGu4roLiho160fTVIwCUrGZna8i"
  },
   {
    "title": "Singapore Chili Crabs",
    "ingredients": [
      "Sauce: ADVERTISEMENT",
      "1/2 cup ketchup ADVERTISEMENT",
      "1/2 cup chicken broth ADVERTISEMENT",
      "1 large egg ADVERTISEMENT",
      "2 tablespoons soy sauce ADVERTISEMENT",
      "2 tablespoons chile-garlic sauce (such as sambal oelek) ADVERTISEMENT",
      "1 tablespoon oyster sauce ADVERTISEMENT",
      "1 tablespoon tamarind paste ADVERTISEMENT",
      "2 teaspoons fish sauce ADVERTISEMENT",
      "2 teaspoons palm sugar ADVERTISEMENT",
      "1/4 cup minced shallot ADVERTISEMENT",
      "6 cloves garlic, minced ADVERTISEMENT",
      "2 tablespoons vegetable oil, or more as needed ADVERTISEMENT",
      "2 tablespoons minced fresh ginger root ADVERTISEMENT",
      "1 tablespoon minced serrano pepper ADVERTISEMENT",
      "2 cooked Dungeness crabs, cleaned and cracked ADVERTISEMENT",
      "2 tablespoons chopped fresh cilantro ADVERTISEMENT",
      "2 tablespoons sliced green onion (green part only) ADVERTISEMENT",
      "ADVERTISEMENT"
    ],
    "instructions": "Whisk ketchup, chicken broth, egg, soy sauce, chile-garlic sauce, oyster sauce, tamarind paste, fish sauce, and palm sugar together in a bowl.\nStir shallots, garlic, oil, ginger, and serrano pepper together in a pot over medium-high heat. Saute until sizzling, about 2 minutes. Add crab to pot, cover the pot with a lid, and shake until crab is completely coated in shallot mixture. Remove lid and cook and stir until heated through, about 3 minutes.\nPour ketchup mixture into pot, reduce heat to medium, and cook and stir until sauce thickens and crab is hot about 5 minutes. Remove from heat; stir in cilantro and green onions.\n",
    "picture_link": "OFp6yXFwzlrkMQ5STffYPllxQvMVLUS"
  }
]

for ind, rep in enumerate(recipes):
    es.index(index="recs", id=ind + 1, document=rep) #create index and add document.


es.indices.refresh(index="recs")