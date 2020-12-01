---
layout: post
title: My recommended Typescript configurations.
tags:
- config
- javascript
- typescript
- development

---
I have recently started to use Typescript in my React projects, although I still have a fair way to go in actually using it fully (currently I am more writing JS in `ts/tsx` files... but that can be for another day).

However I did find I was fighting the swiggly lines in my editor from eslint and prettier and they seemed to be fighting each other in regard to formatting. Having asked around my developer friends and a bit of wrangling myself below is my current config for these projects.

_Note: This is mostly for my own reference and will be updated from time to time as I discover newer options and tools._

First up is my `tsconfig.json`, I expect this to change as I understand the power of typescript.

    /* tsconfig.json */
    {
      "compilerOptions": {
        "target": "ES2020",
        "module": "es2020",
        "jsx": "react",
        "declaration": true,
        "declarationMap": true,
        "strict": true,
        "moduleResolution": "node",
        "allowSyntheticDefaultImports": true,
        "esModuleInterop": true,
        /* Advanced Options */
        "skipLibCheck": true,
        "forceConsistentCasingInFileNames": true
      },
      "include": [
        "./src/**/*"
      ]
    }

Next is my devDependencies snipped from `package.json`

      "devDependencies": {
        "@typescript-eslint/eslint-plugin": "^4.8.2",
        "@typescript-eslint/parser": "^4.8.2",
        "eslint": "^7.1.0",
        "eslint-config-prettier": "^6.11.0",
        "eslint-plugin-prettier": "^3.1.3",
        "prettier": "^2.0.5",
        "typescript": "^4.1.2"
      },

Next is my `.prettierrc` file for formatting

    {
      "trailingComma": "es5",
      "tabWidth": 2,
      "semi": false,
      "singleQuote": false,
      "printWidth": 120
    }

and finally my `.eslintrc.js` file:

    module.exports = {
      parser: `@typescript-eslint/parser`,
      extends: [`plugin:@typescript-eslint/recommended`, `plugin:prettier/recommended`, `prettier/@typescript-eslint`],
      plugins: [`@typescript-eslint`, `prettier`],
      parserOptions: {
        ecmaVersion: 2018, // Allows for the parsing of modern ECMAScript features
        sourceType: `module`, // Allows for the use of imports
      },
      env: {
        browser: true,
        node: true,
      },
      rules: {
        quotes: `off`,
        "@typescript-eslint/quotes": [
          2,
          `backtick`,
          {
            avoidEscape: true,
          },
        ],
        indent: [`error`, 2, { SwitchCase: 1 }],
        "prettier/prettier": [
          `error`,
          {
            trailingComma: `es5`,
            semi: false,
            singleQuote: false,
            printWidth: 120,
          },
        ],
        "@typescript-eslint/explicit-function-return-type": `off`,
      },
    }

I suspect I will need to tweak my `tsconfig` and my `eslint` but for now these are making my development experience somewhat sensible.

If you have any improvements on these files then please let me know!