import { defineConfig } from "vitepress";

export default defineConfig({
  title: "Travelin Vue Documentation",
  description: "Documentation for Travelin Vue Template",
  themeConfig: {
    nav: [{ text: "Home", link: "/" }],
    sidebar: [
      {
        text: "Contents",
        items: [
          { text: "Why Docs", link: "/why-docs" },
          { text: "Project Files", link: "/project-files" },
          { text: "Project Installation", link: "/project-installation" },
          { text: "Code Structure", link: "/code_structure" },
          { text: "Miscellaneous", link: "/miscellaneous" },
        ],
      },
    ],
  },
});
