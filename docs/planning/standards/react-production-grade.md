# React Architecture Guide (Small Team / MVP Edition)

This guide is tailored for small, fast-moving teams. It keeps the high-value patterns and drops the ceremony that slows you down.

---

## Developer Onboarding

### Prerequisites

- Node.js 18+
- VS Code (recommended)

### First-Time Setup

```bash
# 1. Clone and install
git clone <repo-url>
cd snowflame
npm install

# 2. Set up environment
cp .env.example .env
# Fill in your Supabase keys (ask team lead)

# 3. Install VS Code extensions (required for format-on-save)
code --install-extension esbenp.prettier-vscode
code --install-extension dbaeumer.vscode-eslint

# 4. Start dev server
npm run dev
```

### Verify Your Setup

After setup, saving any `.ts` or `.tsx` file should:

1. Auto-format the code (Prettier)
2. Sort imports automatically (React → external → @/ internal)
3. Show lint errors inline (ESLint)

If format-on-save isn't working, check that VS Code is using the workspace settings (`.vscode/settings.json`).

### Key Commands

| Command                | What it does                    |
| ---------------------- | ------------------------------- |
| `npm run dev`          | Start dev server                |
| `npm run build`        | Production build                |
| `npm run lint`         | Check for lint errors           |
| `npm run lint:fix`     | Auto-fix lint errors            |
| `npm run format`       | Format all files                |
| `npm run format:check` | Check formatting (CI uses this) |
| `npm run storybook`    | View UI component library       |
| `npm run test`         | Run tests                       |

### Where to Start

1. **Explore features:** `src/features/` - each folder is a self-contained feature
2. **UI components:** `src/components/ui/` - shared primitives (Button, Input, etc.)
3. **Run Storybook:** `npm run storybook` to see available components

### Before Your First PR

- [ ] `npm run lint` passes
- [ ] `npm run format:check` passes
- [ ] App builds: `npm run build`
- [ ] You've read the code organization rules below

---

## 1. Folder Structure: Feature-Based

Organize by feature, not file type. When you delete a feature, you delete one folder.

```
src/
├── assets/             # Global static assets
├── components/         # Shared UI components (Buttons, Inputs)
├── features/           # Domain logic - the core of your app
│   ├── auth/
│   │   ├── api/        # API calls (or api.ts for simple features)
│   │   ├── components/
│   │   ├── hooks/
│   │   └── index.ts    # Public API - what other features can import
│   └── billing/
├── hooks/              # Shared hooks (useOnClickOutside, etc.)
├── lib/                # Third-party library wrappers
├── pages/              # Route entry points
├── providers/          # React context providers
├── services/           # Shared services (logging, storage)
└── utils/              # Pure utility functions
```

**Small team rule:** Don't create folders until you need them. A feature with 2 files doesn't need 5 subfolders.

---

## 2. Tech Stack

| Category      | Choice                | Why                                                                                          |
| ------------- | --------------------- | -------------------------------------------------------------------------------------------- |
| Language      | TypeScript            | Self-documenting, catches bugs early                                                         |
| Build         | Vite                  | Fast, good DX                                                                                |
| Data fetching | TanStack Query        | Handles caching, loading, errors. Never put API data in Zustand/Redux                        |
| State         | React Query + Context | Query for server state, Context for UI state. Add Zustand only if Context causes perf issues |
| Styling       | Tailwind              | Constraint-based, no magic numbers                                                           |
| Forms         | React Hook Form + Zod | Type-safe validation                                                                         |

**What we skip:** Redux (overkill), CSS-in-JS (slower builds), complex state libraries.

---

## 3. Automation (Keep It Light)

For small teams, heavy automation slows you down more than it helps.

**Do:**

- ESLint in your editor (catches issues as you type)
- CI runs lint + tests on PR (catches issues before merge)
- TypeScript strict mode (catches type errors)

**Skip for now:**

- Husky/lint-staged (slows commits, CI catches the same issues)
- Commitlint (write clear commit messages, don't enforce a schema)
- Pre-push hooks (CI is the gatekeeper)

**Add later when:**

- Team grows beyond 3-4 devs
- You're seeing repeated formatting/lint issues slip through
- You need auto-generated changelogs

---

## 4. Component Patterns

**Colocation over separation.** Keep related code together.

```
features/billing/
├── components/
│   ├── PricingCard.tsx
│   ├── PricingCard.test.tsx    # Test lives with component
│   └── PricingCard.stories.tsx # Story lives with component
├── hooks/
│   └── useSubscription.ts
└── index.ts
```

**Hooks have replaced Container/Presentational.** The old "smart vs dumb component" pattern is less relevant now. Instead:

- Components fetch their own data via hooks
- Extract shared logic into custom hooks
- Keep components focused on one thing

**Avoid prop drilling:** If passing props 3+ levels deep, use:

1. Composition (pass components as children)
2. Context (for truly global UI state)
3. React Query (for server state - components fetch what they need)

---

## 5. Barrel Exports

Use `index.ts` to control what a feature exposes. This prevents accidental coupling.

```typescript
// features/billing/index.ts
export { PricingCards } from "./components/PricingCards";
export { useSubscription } from "./hooks/useSubscription";
export type { SubscriptionPlan } from "./types";

// Don't export internal helpers
```

**Import from the barrel:**

```typescript
// Good
import { useSubscription } from "@/features/billing";

// Avoid - breaks encapsulation
import { useSubscription } from "@/features/billing/hooks/useSubscription";
```

**Watch out:** Barrel exports can cause circular imports. If you hit issues, import directly from the file.

---

## 6. Documentation (Minimal)

**Do:**

- Storybook for shared UI components (prevents rebuilding existing components)
- Inline code comments for non-obvious logic
- README in complex features if needed
- ADRs (Architecture Decision Records) - These are to explain why we did things a specific way, technology used, best practices and intentions etc

**Skip:**

- Extensive JSDoc - TypeScript types are your documentation
- Separate docs for obvious patterns

---

## 7. What This Guide Doesn't Cover (Add When Needed)

- **Error boundaries** - Add when you have complex error states
- **Suspense** - Add when you need streaming/concurrent features
- **Code splitting** - Vite handles this well by default, optimize when bundle size matters
- **Testing strategy** - Start with integration tests on critical paths, don't aim for coverage %
- **Performance** - Profile first, optimize second. Don't premature optimize

---

## Summary: Small Team Principles

1. **Add structure when it hurts** - Don't create folders/patterns until you feel the pain
2. **CI is your gatekeeper** - Let automation run on PR, not on every commit
3. **Colocation > separation** - Keep related code together
4. **TypeScript + React Query** - These two catch 80% of bugs before they happen
