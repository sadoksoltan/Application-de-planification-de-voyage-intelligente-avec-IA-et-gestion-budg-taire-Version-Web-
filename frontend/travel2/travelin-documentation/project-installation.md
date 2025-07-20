---
outline: deep
---

# Project Installation

This page details on how to set up the project.

Prerequisites:

- [Node.js (v20 or later)](https://nodejs.org)
- [Visual Studio Code](https://code.visualstudio.com/) (or any other editor)
- [Git](https://git-scm.com/)

Follow along the steps to set up the project:

1. After downloading project files, open the project folder in visual studio code.
2. Run `npm install` command in the terminal. This will install all the necessary dependencies and dev-dependencies for the project.
3. Run `npm run dev` for running the Vue development server at `localhost:5173`.
4. Open **localhost:5173** in the browser and **here we go - boom**.
5. Feel free to make changes to the code according to your project needs.

::: info Info
Remember to install [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) extension for VSCode which provides TypeScript support in Vue-based projects.
:::

## Project Dependencies

|                           Package Name                           | Version |
| :--------------------------------------------------------------: | :-----: |
| [@splidejs/splide](https://splidejs.com/guides/getting-started/) | ^4.1.4  |
|     [awesome-image-viewer](https://awesome-components.com/)      | ^1.0.60 |
|              [bootstrap](https://getbootstrap.com/)              | ^5.3.2  |
|         [vue](https://vuejs.org/guide/quick-start.html)          | ^3.3.11 |
|     [vue-router](https://router.vuejs.org/installation.html)     | ^4.2.5  |

## Project Dev Dependencies

|                              Package Name                              | Version  |
| :--------------------------------------------------------------------: | :------: |
|        [@types/node](https://www.npmjs.com/package/@types/node)        | ^20.11.5 |
| [@vitejs/plugin-vue](https://www.npmjs.com/package/@vitejs/plugin-vue) |  ^4.5.2  |
|               [path](https://www.npmjs.com/package/path)               | ^0.12.7  |
|         [typescript](https://www.npmjs.com/package/typescript)         |  ^5.2.2  |
|               [vite](https://www.npmjs.com/package/vite)               |  ^5.0.8  |
|            [vue-tsc](https://www.npmjs.com/package/vue-tsc)            | ^1.8.25  |

::: info Info
Always install the latest dependencies and dev-dependencies to resolve known issues, errors, or bugs that are associated with the previous version.

For this, you can run command `npm oudated` to see the list of outdated packages in the terminal.

Run `npm update` command in the terminal to update all dependencies to the latest version. You can check out [this blog](https://www.freecodecamp.org/news/how-to-update-npm-dependencies/) article for more information.
:::

## Production Deployment

When you are ready to deploy, run `npm run build` command in the terminal to build the production version of the project. When build completes, a `dist` folder is created in your project root directory which is a minified version of your project which is now ready to be deployed.

For deployment, you can choose any hosting providers, including [Vercel](https://vercel.com/), [Netlify](https://www.netlify.com/), [CPanel](https://cpanel.net/), [Render](https://render.com/), etc.

Just follow along the production deployment process of the hosting provider of your choice for deploying the project successfully.

::: info Info
When you run `npm run build` in the terminal, the `npx vue-tsc --noEmit` command is also run alongside it. The `vue-tsc` is a utility for command line type checking and type declaration generation in a TypeScript-based Vue projects.

This means variables, components, assets, or any other files which are imported but not used in the file will be thrown as errors by `vue-tsc` and the production build will fail.

Therefore, always make sure you don't have these any errors before running `npm run build`.
:::
