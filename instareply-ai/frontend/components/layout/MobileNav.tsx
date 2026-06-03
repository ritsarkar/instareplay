import { Menu } from "lucide-react";

export function MobileNav() {
  return (
    <button className="grid h-10 w-10 place-items-center rounded-lg border border-slate-200 text-slate-700 md:hidden" type="button">
      <Menu aria-hidden="true" size={20} />
      <span className="sr-only">Open navigation</span>
    </button>
  );
}
