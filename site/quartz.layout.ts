import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

// ── SHARED COMPONENTS (all pages) ──────────────────────────────

export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [
    Component.ChatWidget({
      wiki: "naval",
      apiUrl: "https://api-production-4224.up.railway.app",
    }),
  ],
  footer: Component.Footer({
    links: {
      "Creative Intelligence Agency": "https://creativeintel.agency",
      "Skill Stack": "https://skillstack.md",
      "GitHub": "https://github.com/cdeistopened",
    },
  }),
}

// ── CONTENT PAGE LAYOUT (single articles) ──────────────────────

export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.ChatBanner({
      label: "Ask Naval",
      description: "Chat with an AI that's read 160 episodes",
    }),
    Component.ConditionalRender({
      component: Component.Breadcrumbs(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ArticleTitle(),
    Component.ContentMeta(),
    Component.TagList(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
        { Component: Component.ReaderMode() },
      ],
    }),
    Component.Explorer({
      folderDefaultState: "open",
      filterFn: (node) => {
        return node.slugSegment !== "tags"
      },
      sortFn: (a, b) => {
        // Themes/frameworks first, then skills, then episodes
        const order = ["frameworks", "skills", "indexes"]
        const aIdx = order.indexOf(a.slugSegment ?? "")
        const bIdx = order.indexOf(b.slugSegment ?? "")
        if (aIdx !== -1 && bIdx !== -1) return aIdx - bIdx
        if (aIdx !== -1) return -1
        if (bIdx !== -1) return 1
        return a.displayName.localeCompare(b.displayName)
      },
    }),
  ],
  right: [
    Component.Graph(),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Backlinks(),
  ],
}

// ── LIST PAGE LAYOUT (folders, tags) ───────────────────────────

export const defaultListPageLayout: PageLayout = {
  beforeBody: [
    Component.Breadcrumbs(),
    Component.ArticleTitle(),
    Component.ContentMeta(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
      ],
    }),
    Component.Explorer({
      folderDefaultState: "open",
      filterFn: (node) => {
        return node.slugSegment !== "tags"
      },
      sortFn: (a, b) => {
        const order = ["frameworks", "skills", "indexes"]
        const aIdx = order.indexOf(a.slugSegment ?? "")
        const bIdx = order.indexOf(b.slugSegment ?? "")
        if (aIdx !== -1 && bIdx !== -1) return aIdx - bIdx
        if (aIdx !== -1) return -1
        if (bIdx !== -1) return 1
        return a.displayName.localeCompare(b.displayName)
      },
    }),
  ],
  right: [],
}
