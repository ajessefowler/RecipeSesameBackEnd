from datetime import datetime
import enum
from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")

recipes =  [
    {
    "title": "Slow Cooker Chicken and Dumplings",
    "ingredients": [
      "4 skinless, boneless chicken breast halves",
      "2 tablespoons butter",
      "2 (10.75 ounce) cans condensed cream of chicken soup",
      "1 onion, finely diced",
      "2 (10 ounce) packages refrigerated biscuit dough, torn into pieces"
    ],
    "instructions": "Place the chicken, butter, soup, and onion in a slow cooker, and fill with enough water to cover.\nCover, and cook for 5 to 6 hours on High. About 30 minutes before serving, place the torn biscuit dough in the slow cooker. Cook until the dough is no longer raw in the center.\n",
    "picture_link": "55lznCYBbs2mT8BTx6BTkLhynGHzM.S"
  },
  {
    "title": "Awesome Slow Cooker Pot Roast",
    "ingredients": [
      "2 (10.75 ounce) cans condensed cream of mushroom soup",
      "1 (1 ounce) package dry onion soup mix",
      "1 1/4 cups water",
      "5 1/2 pounds pot roast"
    ],
    "instructions": "In a slow cooker, mix cream of mushroom soup, dry onion soup mix and water. Place pot roast in slow cooker and coat with soup mixture.\nCook on High setting for 3 to 4 hours, or on Low setting for 8 to 9 hours.\n",
    "picture_link": "QyrvGdGNMBA2lDdciY0FjKu.77MM0Oe"
  },
  {
    "title": "Brown Sugar Meatloaf",
    "ingredients": [
      "1/2 cup packed brown sugar",
      "1/2 cup ketchup",
      "1 1/2 pounds lean ground beef",
      "3/4 cup milk",
      "2 eggs",
      "1 1/2 teaspoons salt",
      "1/4 teaspoon ground black pepper",
      "1 small onion, chopped",
      "1/4 teaspoon ground ginger",
      "3/4 cup finely crushed saltine cracker crumbs"
    ],
    "instructions": "Preheat oven to 350 degrees F (175 degrees C). Lightly grease a 5x9 inch loaf pan.\nPress the brown sugar in the bottom of the prepared loaf pan and spread the ketchup over the sugar.\nIn a mixing bowl, mix thoroughly all remaining ingredients and shape into a loaf. Place on top of the ketchup.\nBake in preheated oven for 1 hour or until juices are clear.\n",
    "picture_link": "LVW1DI0vtlCrpAhNSEQysE9i/7rJG56"
  },
  {
    "title": "Best Chocolate Chip Cookies",
    "ingredients": [
      "1 cup butter, softened",
      "1 cup white sugar",
      "1 cup packed brown sugar",
      "2 eggs",
      "2 teaspoons vanilla extract",
      "3 cups all-purpose flour",
      "1 teaspoon baking soda",
      "2 teaspoons hot water",
      "1/2 teaspoon salt",
      "2 cups semisweet chocolate chips",
      "1 cup chopped walnuts"
    ],
    "instructions": "Preheat oven to 350 degrees F (175 degrees C).\nCream together the butter, white sugar, and brown sugar until smooth. Beat in the eggs one at a time, then stir in the vanilla. Dissolve baking soda in hot water. Add to batter along with salt. Stir in flour, chocolate chips, and nuts. Drop by large spoonfuls onto ungreased pans.\nBake for about 10 minutes in the preheated oven, or until edges are nicely browned.\n",
    "picture_link": "0SO5kdWOV94j6EfAVwMMYRM3yNN8eRi"
  },
  {
    "title": "Homemade Mac and Cheese Casserole",
    "ingredients": [
      "8 ounces whole wheat rotini pasta",
      "3 cups fresh broccoli florets",
      "1 medium onion, chopped",
      "3 cloves garlic, minced",
      "4 tablespoons butter, divided",
      "2 tablespoons all-purpose flour",
      "1/4 teaspoon salt",
      "1/8 teaspoon ground black pepper",
      "2 1/2 cups milk",
      "8 ounces Cheddar cheese, shredded",
      "4 ounces reduced-fat cream cheese, cubed and softened",
      "1/2 cup fine dry Italian-seasoned bread crumbs",
      "Reynolds Wrap\u00ae Non Stick Aluminum Foil"
    ],
    "instructions": "Preheat oven to 350 degrees F. Line a 2-quart casserole dish with Reynolds Wrap(R) Pan Lining Paper, parchment side up. No need to grease dish.\nCook the pasta in a large saucepan according to the package directions, adding the broccoli for the last 3 minutes of cooking. Drain. Return to the saucepan and set aside.\nCook the onion and garlic in 2 tablespoons hot butter in a large skillet 5 to 7 minutes or until tender. Stir in flour, salt, and black pepper. Add the milk all at once. Cook and stir over medium heat until slightly thickened and bubbly. Add cheddar cheese and cream cheese, stirring until melted. Pour cheese sauce over the pasta and broccoli and stir until well combined.\nMelt the remaining 2 tablespoons butter and mix with the bread crumbs in a small bowl. Transfer the pasta mixture to the prepared casserole dish. Top with the buttery bread crumbs.\nBake, uncovered, about 25 minutes or until bubbly and internal temperature is 165 degrees F. Let stand for 10 minutes before serving.\n",
    "picture_link": "YCnbhplMgiraW4rUXcybgSEZinSgljm"
  },
  {
    "title": "Banana Banana Bread",
    "ingredients": [
      "2 cups all-purpose flour",
      "1 teaspoon baking soda",
      "1/4 teaspoon salt",
      "1/2 cup butter",
      "3/4 cup brown sugar",
      "2 eggs, beaten",
      "2 1/3 cups mashed overripe bananas"
    ],
    "instructions": "Preheat oven to 350 degrees F (175 degrees C). Lightly grease a 9x5 inch loaf pan.\nIn a large bowl, combine flour, baking soda and salt. In a separate bowl, cream together butter and brown sugar. Stir in eggs and mashed bananas until well blended. Stir banana mixture into flour mixture; stir just to moisten. Pour batter into prepared loaf pan.\nBake in preheated oven for 60 to 65 minutes, until a toothpick inserted into center of the loaf comes out clean. Let bread cool in pan for 10 minutes, then turn out onto a wire rack.\n",
    "picture_link": "jRnWGDXDdyOg3rta4/HVAR2rD19XubC"
  },
  {
    "title": "Chef John's Fisherman's Pie",
    "ingredients": [
      "For potato crust:",
      "3 russet potatoes, peeled and cut into chunks",
      "3 tablespoons butter",
      "1 pinch freshly grated nutmeg",
      "salt and ground black pepper to taste",
      "1 pinch cayenne pepper, or to taste",
      "1/2 cup milk",
      "For the spinach:",
      "2 teaspoons olive oil",
      "12 ounces baby spinach leaves",
      "For the sauce:",
      "3 tablespoons butter",
      "3 tablespoons all-purpose flour",
      "2 cloves garlic, minced",
      "2 cups cold milk, divided",
      "2 teaspoons lemon zest",
      "For the rest:",
      "1 tablespoon butter",
      "salt and ground black pepper to taste",
      "1 pinch cayenne pepper, or to taste",
      "2 pounds boneless cod fillets",
      "1/2 lemon, juiced",
      "1 tablespoon chopped fresh chives for garnish"
    ],
    "instructions": "Bring a large saucepan of salted water and to a boil; add russet potatoes to boiling water and cook until very tender, about 20 minutes. Drain well. Mash in 3 tablespoons butter until thoroughly combined. Season with nutmeg, salt, black pepper, and cayenne pepper to taste. Mash 1/2 cup milk into potato mixture until smooth.\nDrizzle olive oil in a large Dutch oven over medium-high heat, add spinach, and season with a big pinch of salt. Cook, stirring occasionally, until spinach has wilted, about 1 minute. Transfer to a bowl lined with paper towels to wick away excess moisture.\nHeat 3 tablespoons butter and flour in a saucepan over medium heat; whisk mixture to a smooth paste. Cook, stirring constantly, until mixture has a nutty smell and is slightly browned, about 2 minutes. Add chopped garlic; whisk until fragrant, 10 to 20 seconds.\nWhisk 1 cup cold milk into flour mixture; cook until thickened. Whisk in remaining 1 cup milk and lemon zest. Bring white sauce to a gentle simmer, whisking constantly; season with salt. Turn heat to very low and keep sauce warm.\nPreheat oven to 375 degrees F (190 degrees C). Grease an 8x12-inch casserole dish with 1 tablespoon butter.\nSeason buttered pan with salt, black pepper, and cayenne pepper. Lay boneless cod fillets into the pan in a single layer. Season tops of fillets with more salt, black pepper, and cayenne pepper. Spread spinach evenly over fish and drizzle with lemon juice. Spoon white sauce over spinach; give casserole dish several taps and shakes to eliminate bubbles.\nDrop mashed potatoes by heaping spoonfuls over the casserole and spread smoothly to cover. Place dish onto a rimmed baking sheet to catch spills.\nBake in the preheated oven until bubbling, about 40 minutes. Turn on oven's broiler and broil until potato crust has a golden brown top, about 2 minutes. Fish should flake easily. Let stand 10 minutes before serving. Garnish with a sprinkle of chives.\n",
    "picture_link": "aUca10AaD8T2yYvcLOgH/UJlR5/OhOe"
  },
  {
    "title": "Mom's Zucchini Bread",
    "ingredients": [
      "3 cups all-purpose flour",
      "1 teaspoon salt",
      "1 teaspoon baking soda",
      "1 teaspoon baking powder",
      "1 tablespoon ground cinnamon",
      "3 eggs",
      "1 cup vegetable oil",
      "2 1/4 cups white sugar",
      "3 teaspoons vanilla extract",
      "2 cups grated zucchini",
      "1 cup chopped walnuts"
    ],
    "instructions": "Grease and flour two 8 x 4 inch pans. Preheat oven to 325 degrees F (165 degrees C).\nSift flour, salt, baking powder, soda, and cinnamon together in a bowl.\nBeat eggs, oil, vanilla, and sugar together in a large bowl. Add sifted ingredients to the creamed mixture, and beat well. Stir in zucchini and nuts until well combined. Pour batter into prepared pans.\nBake for 40 to 60 minutes, or until tester inserted in the center comes out clean. Cool in pan on rack for 20 minutes. Remove bread from pan, and completely cool.\n",
    "picture_link": "YdgEVyLVffZgh9NZPN3Eqj6MaX8KdzK"
  },
   {
    "title": "The Best Rolled Sugar Cookies",
    "ingredients": [
      "1 1/2 cups butter, softened",
      "2 cups white sugar",
      "4 eggs",
      "1 teaspoon vanilla extract",
      "5 cups all-purpose flour",
      "2 teaspoons baking powder",
      "1 teaspoon salt"
    ],
    "instructions": "In a large bowl, cream together butter and sugar until smooth. Beat in eggs and vanilla. Stir in the flour, baking powder, and salt. Cover, and chill dough for at least one hour (or overnight).\nPreheat oven to 400 degrees F (200 degrees C). Roll out dough on floured surface 1/4 to 1/2 inch thick. Cut into shapes with any cookie cutter. Place cookies 1 inch apart on ungreased cookie sheets.\nBake 6 to 8 minutes in preheated oven. Cool completely.\n",
    "picture_link": "UrgvDGu4roLiho160fTVIwCUrGZna8i"
  },
   {
    "title": "Singapore Chili Crabs",
    "ingredients": [
      "Sauce:",
      "1/2 cup ketchup",
      "1/2 cup chicken broth",
      "1 large egg",
      "2 tablespoons soy sauce",
      "2 tablespoons chile-garlic sauce (such as sambal oelek)",
      "1 tablespoon oyster sauce",
      "1 tablespoon tamarind paste",
      "2 teaspoons fish sauce",
      "2 teaspoons palm sugar",
      "1/4 cup minced shallot",
      "6 cloves garlic, minced",
      "2 tablespoons vegetable oil, or more as needed",
      "2 tablespoons minced fresh ginger root",
      "1 tablespoon minced serrano pepper",
      "2 cooked Dungeness crabs, cleaned and cracked",
      "2 tablespoons chopped fresh cilantro",
      "2 tablespoons sliced green onion (green part only)"
    ],
    "instructions": "Whisk ketchup, chicken broth, egg, soy sauce, chile-garlic sauce, oyster sauce, tamarind paste, fish sauce, and palm sugar together in a bowl.\nStir shallots, garlic, oil, ginger, and serrano pepper together in a pot over medium-high heat. Saute until sizzling, about 2 minutes. Add crab to pot, cover the pot with a lid, and shake until crab is completely coated in shallot mixture. Remove lid and cook and stir until heated through, about 3 minutes.\nPour ketchup mixture into pot, reduce heat to medium, and cook and stir until sauce thickens and crab is hot about 5 minutes. Remove from heat; stir in cilantro and green onions.\n",
    "picture_link": "OFp6yXFwzlrkMQ5STffYPllxQvMVLUS"
  }, 
  {
    "instructions": "Watch how to make this recipe.\nPut an oven rack in the center of the oven. Preheat the oven to 400 degrees F.\nSpray 2 baking sheets with cooking spray. Lay the pancetta in a single layer on the prepared baking sheets and bake until crispy and brown, about 12 to 14 minutes. Drain on paper towels. Cool for 5 minutes and crumble. Set aside.\nIn a food processor, combine the butter, cheeses, salt, and 1 tablespoon vegetable oil. Blend until smooth, adding extra oil, as needed, until the mixture is spreadable. Add the spinach and pulse until just combined.\nPreheat a panini maker. Spread the cheese mixture over 8 slices of bread. Top with the crumbled pancetta. Put the remaining bread slices on top. Grill the sandwiches, 2 at a time, until golden and crispy, about 3 to 4 minutes. Cool for 2 minutes, then cut each sandwich in half and arrange on a platter.",
    "ingredients": [
      "Vegetable oil cooking spray",
      "6 ounces pancetta, cut into 1/8-inch-thick slices",
      "1/2 cup (1 stick) unsalted butter, at room temperature",
      "2 cups (8 ounces) shredded Monterey Jack cheese",
      "2 cups (8 ounces) shredded mild Cheddar",
      "1 teaspoon kosher salt",
      "1 tablespoon vegetable or canola oil, plus extra, as needed",
      "2 packed cups coarsely chopped baby spinach",
      "16 (1/3-inch-thick) slices country-style white bread"
    ],
    "title": "Grilled Cheese with Spinach and Pancetta",
    "picture_link": "7.QEdieuqNCxdlIA4hZLkBTgk/iyXD6"
  },
  {
    "instructions": "Par-bake the crust: Preheat the oven to 400 degrees F. Use both pie crusts to cover the bottom and sides of a 13-by-9-inch casserole dish. Patchwork works, just cover the holes. Dock by pricking holes in the crust with a fork all over the bottom. Bake until lightly golden, 15 to 20 minutes.\nFor the fruit filling: In a large bowl, stir together the granulated sugar, brown sugar, flour, almond extract, pumpkin pie spice, lemon zest and lemon juice. Divide the mixture among the smaller bowls: 3/4 cup in the first, 1/2 cup in the second and 1/4 cup in the third. (Think of the 3 bears: poppa, momma and baby bear bowls.)\nPut the cranberries in the poppa bear bowl; in the momma bear bowl, add the apples; and in the baby bear bowl, add the figs. (Do you need a translation? Add cranberries to the bowl with the most flour mixture, apples to the bowl with 1/2 cup of the flour mixture, and the figs to the bowl with the least amount of the flour mixture.) Stir each bowl independently, unless you\u00bfre an octopus.\nFor the streusel topping: In a food processor add the flour, brown sugar, granulated sugar, butter, and a pinch of salt. Blend until crumbly, taste and add more salt if needed. Pour into a small bowl with the almonds and stir.\nPreheat the oven to 400 degrees F. Pour the fruit filling into the prepared crust, dividing it into thirds with the apples in the middle and the figs and cranberries on either side. Top evenly with the streusel mixture. Cover the pie edges with aluminum foil so they don\u00bft overcook. Bake until the top is golden brown and the fruit is beginning to bubble around the edges, 40 to 50 minutes. Serve warm with the bourbon whipped cream.\nWhisk the cream in a large bowl until soft peaks form. Add the bourbon and sugar and continue whisking until the cream holds slightly stiff peaks when the whisk is removed from the bowl. Refrigerate and serve cold.",
    "ingredients": [
      "2 pre-made pie crusts (the kind that roll up, not pre-formed)",
      "1 cup granulated sugar",
      "1/4 cup light brown sugar",
      "1/4 cup plus 2 tablespoons all-purpose flour",
      "1/2 teaspoon almond extract",
      "1/2 teaspoon pumpkin pie spice",
      "Zest of 2 lemons",
      "2 tablespoons fresh lemon juice",
      "1 pound fresh or frozen and thawed cranberries, picked through to remove stems and field debris",
      "4 Granny Smith apples, cored, peeled, and chopped",
      "15 fresh Black Mission or Brown Turkey figs, stemmed and sliced",
      "2 cups all-purpose flour",
      "1 3/4 cups packed light brown sugar",
      "1/4 cup granulated sugar",
      "1 1/2 sticks (12 tablespoons) ice cold unsalted butter, cut into teeny weeny cubes",
      "Kosher salt",
      "1 cup almonds, roughly chopped",
      "Sunny's Bourbon Whipped Cream, for serving, recipe follows",
      "1 cup heavy cream",
      "1 tablespoon bourbon",
      "1 tablespoon sugar"
    ],
    "title": "Sunny's Cranberry, Apple and Fig Streusel Tart",
    "picture_link": "ea5AxIMPGbTNz05gSoYomjBq94xg0Rm"
  }, 
  {
    "instructions": "Special equipment: an immersion blender and meat mallet\nBring a large pot of salted water to a boil. Add the broccoli and cook until just crisp-tender. Plunge into an ice bath to stop the cooking. Drain and reserve.\nBring a large pot of salted water to a boil and cook the pasta according to the package directions. Drain and reserve.\nPlace the oven rack in the middle position and preheat the oven to high broil.\nCreate a standard breading station in 3 separate 8-by-8-inch pans: Combine the flour, 1 tablespoon salt and 2 teaspoons pepper into the first pan. Whisk together the eggs and the milk in the second pan. Place the breadcrumbs in the third pan.\nTrim any fat from the edges of the chicken breast and place each breast between 2 pieces of plastic wrap. With a meat mallet, pound out each breast until it is an even 1/4 inch thick.\nDredge each breasts using the standard breading: First in the flour, then in the egg wash and finally in the breadcrumbs, making sure to coat the entire breast.\nHeat a large skillet over high heat until it begins to smoke and then reduce the heat to medium. Add 2 tablespoons oil to the pan and gently place 2 breasts in the pan. Cook the chicken on the first side until the breading is golden brown, about 5 minutes. Gently turn the breasts over and cook until the breading is golden brown on the other side, about 5 minutes. Remove the chicken breasts to a pan lined with paper towels. Repeat with the remaining chicken breasts, changing the oil between each batch.\nPlace the chicken breasts on rimmed baking sheets. Top each breast with 3 pieces of the broccolini and 2 slices of the mozzarella. Bake until the cheese is melted and begins to brown, 5 to 10 minutes.\nFor plating: Bring the Tomato Sauce to a simmer in a large skillet. Add the pasta and cook until the pasta and sauce are hot.\nDivide the pasta and sauce among 6 plates, mounding it in the center of each plate. Place a finished chicken breast on top of each mound. Sprinkle each plate with 1 tablespoon Parmesan and 1 teaspoon chopped parsley.\nCombine the whole tomatoes and their liquid, the olive oil, onion, basil, oregano, salt, pepper and 4 cloves garlic in a large bowl or 2-gallon container and puree with an immersion blender until smooth.\nHeat a large saute pan over high heat until it begins to smoke. Reduce the heat to medium, add the grapeseed oil and remaining 4 cloves garlic and quickly saute. Add the diced tomatoes and saute for 1 to 2 minutes. Add the pureed tomato sauce and bring to a simmer. Cook for 15 minutes, remove from the heat. Bring back to a simmer when you are ready to plate. Yield: 6 servings",
    "ingredients": [
      "Kosher salt and freshly ground black pepper",
      "18 pieces broccolini",
      "2 pounds spaghetti",
      "2 cups all-purpose flour",
      "6 large eggs",
      "1 cup milk",
      "3 cups panko breadcrumbs",
      "Six 6-ounce boneless skinless chicken breast",
      "1 cup grapeseed oil",
      "12 slices aged (low-moisture) mozzarella",
      "1 quart Tomato Sauce, recipe follows",
      "6 tablespoons grated Parmesan",
      "2 tablespoons chopped fresh parsley",
      "5 cups canned whole San Marzano tomatoes, plus liquid from the can",
      "1/2 cup extra-virgin olive oil",
      "1/2 cup diced yellow onion",
      "2 tablespoons fresh basil, chopped",
      "2 tablespoons fresh oregano, chopped",
      "1 tablespoon kosher salt",
      "2 teaspoons freshly ground black pepper",
      "8 cloves garlic",
      "2 tablespoons grapeseed oil",
      "3 cups canned diced San Marzano tomatoes"
    ],
    "title": "Chicken Parmesan",
    "picture_link": "Q5myPx4uVERzjAn.2qTcacekwjgFtfW"
  },
  {
    "instructions": "For the dough: Combine the flour, sugar and 1/2 teaspoon salt in a food processor and pulse until mixed. Add about a third of the chilled butter and process until thoroughly combined with no visible chunks of butter (the mixture will be slightly yellow). Add the remaining butter and pulse until the mixture resembles a very coarse meal with pea-size bits of butter. Add the vinegar in a single pulse. Gradually add 2 tablespoons ice water through the feed tube, pulsing just until evenly combined. Squeeze a handful of the dough together-it should just hold its shape and be a little crumbly. If still very powdery, pulse again, adding up to 2 tablespoons ice water.\nTurn the dough out onto a work surface and pat together into a flat disk about 1/2-inch thick. Wrap tightly in plastic wrap. Refrigerate until firm, at least 1 hour or up to 2 days.\nFor the galette: Adjust an oven rack to the lower third position and preheat the oven to 400 degrees F.\nToss the yellow squash and zucchini with 3/4 teaspoon salt in a bowl. Let sit for 15 minutes to draw out a good amount of water from the vegetables.\nMeanwhile, lay out the bacon slices in a large skillet. Place over medium heat and cook partially, flipping occasionally, to render out some fat but not to brown or crisp up, about 5 minutes. Transfer to a cutting board; let cool slightly, then cut into 1/2-inch pieces. Reserve the bacon fat in the pan.\nPat the squash slices dry; place in a large bowl with the red onion slices and toss with olive oil, 1/2 teaspoon salt and a few grinds of pepper.\nLet the dough stand at room temperature for a few minutes until slightly softened. Roll out on a lightly floured surface into a 12- to 13-inch circle, about 1/8-inch thick. Transfer to an ungreased baking sheet. Sprinkle the mozzarella and Parmesan on the circle, leaving empty a 1 1/2-inch border all around. Fan the squash, zucchini and onions in a circle, then scatter the bacon on top. Fold up the edges of the dough, pleating, to overlap the filling. Brush the dough border with the egg wash. Drizzle any bacon fat over the filling.\nBake until golden brown all over and the filling is bubbly, 45 to 50 minutes. Brush the galette with a little vinegar while still warm and serve.",
    "ingredients": [
      "1 3/4 cups all-purpose flour, plus more for rolling",
      "1 teaspoon sugar",
      "Kosher salt",
      "10 tablespoons cold unsalted butter, cut into 1/2-inch cubes",
      "1 teaspoon white vinegar",
      "1 medium yellow squash (10 ounces), sliced into 1/8-inch thin rounds",
      "1 medium zucchini (10 ounces), sliced into 1/8-inch thin rounds",
      "Kosher salt and freshly ground black pepper",
      "4 slices bacon",
      "1 small red onion, sliced thinly and separated into rings",
      "2 tablespoons extra-virgin olive oil",
      "1 cup shredded mozzarella",
      "3 tablespoons grated Parmesan",
      "1 egg, beaten",
      "Red wine vinegar, for brushing"
    ],
    "title": "Summer Squash and Bacon Galette",
    "picture_link": "9.qJlYGPwVHz9ztS23frN3BIYLIScli"
  }, 
  {
    "instructions": "Preheat the oven to 250 degrees F.\nHeat a cast iron skillet over medium-high to high heat. Put a platter in the oven to warm.\nCombine all the spices in a small bowl. Score the skin of the fish with several shallow hash marks using a very sharp knife. Season the fish on both sides with lots of salt and pepper, to taste, and rub both sides with spices.\nAdd the oil to the hot pan and cook the fish in 2 batches, until firm, about 4 minutes on each side. Transfer the fillets to the warm platter. Serve with lemon wedges and garnish with parsley or chives.",
    "ingredients": [
      "1 tablespoon smoked sweet paprika, a palmful",
      "1 1/2 teaspoons granulated onion, half a palmful",
      "1 1/2 teaspoons granulated garlic, half a palmful",
      "1 teaspoon coriander, half a palmful",
      "1 teaspoon dried mustard",
      "1/4 teaspoon cayenne pepper",
      "4 fillets black bass, skin-on",
      "Salt and freshly ground black pepper",
      "2 tablespoons vegetable oil",
      "Lemon wedges, for garnish",
      "Chopped parsley leaves or chives, for garnish"
    ],
    "title": "Smoky-Spicy Bass",
    "picture_link": "Vw7ZGo.0jIFoEXqFJmU81LIyizTUcG2"
  }
]

for ind, rep in enumerate(recipes):
    es.index(index="recs", id=ind + 1, document=rep) #create index and add document.


es.indices.refresh(index="recs")