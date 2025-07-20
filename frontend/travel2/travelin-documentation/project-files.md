---
outline: deep
---

# Project Files - Overview

This page explains the project files in brief so that you can understand how this project was set up.

The project files can be divided into four types: **assets**, **components**, **pages**, and **routes**.

## Assets

The project assets include `images,`, `fonts`, `icons`, etc. which are placed under the `src/assets/` directory in the project folder.

Feel free to explore these assets and use them anyway you want.

## Components

The project components include reusable components (part or section of a page) that can be used in another page, located under the `src/pages/components/` directory in the project folder.

Feel free to create as many components depending upon your needs.

## Pages

The project consists of total 23 pages that are created under the `src/pages` directory in the project folder.

Feel free to explore these components and use them anyway you want.

## Routes

The project routes are defined in the `src/routes/index.ts` file where routes are mapped into pages for navigation.

Here's the quick overview of routes that are mapped into pages:

| Pages                 |        Route        |
| --------------------- | :-----------------: |
| Home.vue              |          /          |
| About.vue             |       /about        |
| DestinationList.vue   |  /destination-list  |
| DestinationDetail.vue | /destination-detail |
| TourLists.vue         |     /tour-list      |
| TourGrid.vue          |     /tour-grid      |
| TourSingle.vue        |    /tour-single     |
| Team.vue              |        /team        |
| Booking.vue           |      /booking       |
| Confirmation.vue      |    /confirmation    |
| Serivces.vue          |      /services      |
| ServiceDetail.vue     |   /service-detail   |
| GalleryMasonary.vue   |      /gallery1      |
| 404Error.vue          |        /404         |
| Login.vue             |       /login        |
| CommingSoon.vue       |     /comingsoon     |
| Testimonial.vue       |    /testimonial     |
| Contact.vue           |      /contact       |
| FAQ.vue               |        /faq         |
| PostGrid1.vue         |    /post-grid-1     |
| PostList1.vue         |    /post-list-1     |
| PostDetail1.vue       |      /detail-1      |

::: info Info
All routes are lazy-loaded by default - meaning a page will only load when an user actually visit the page. This helps to keep JS bundle size low by splitting code into different chunks and improve initial loading time experience for pages.
:::

## Other Files

These are the files that can be found under the `src` directory of the project folder.

### App.vue

The `App.vue` is the entry Vue component of the project.

### main.js

The `main.js` is the entry point of an Vue application.

The `App.vue`, `style.css`, `smooth.js`, etc. all are referenced here.

### smooth.js

The `smooth.js` file is used for smooth scroll animation when scrolling up or down with a mouse.

### style.css

The `style.css` file is the main CSS file for the project. All CSS rules are defined here with comments.

Additional CSS are written in `<style></style>` part of the component whenever necessary or appropriate.

Feel free to explore these CSS rules and modify any CSS according to your project needs.

### vite.env.d.ts

The `vite.env.d.ts` file is not related to the project but used by Vite for referencing environment variables and for TypeScript intellisense in the project.

In the next page, we'll discuss the installation steps of the project.
