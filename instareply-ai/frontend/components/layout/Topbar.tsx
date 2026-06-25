import { MobileNav } from "@/components/layout/MobileNav";
import { Bell, Search } from "lucide-react";

export function Topbar() {
  return (
    <header className="sticky top-0 z-20 flex h-16 items-center justify-between border-b border-slate-200 bg-white/80 backdrop-blur-md px-4 md:px-6 shadow-sm">
      <div className="flex items-center gap-4">
        <MobileNav />
        <div className="hidden md:flex items-center gap-2 text-sm text-slate-500 bg-slate-100/80 px-3 py-1.5 rounded-md border border-slate-200 transition-colors hover:bg-slate-100 hover:border-slate-300 cursor-text">
          <Search className="h-4 w-4 text-slate-400" />
          <span>Search customers, messages...</span>
          <kbd className="ml-4 hidden sm:inline-block rounded border border-slate-300 bg-slate-50 px-1.5 text-[10px] font-medium text-slate-500">Ctrl K</kbd>
        </div>
      </div>
      
      <div className="flex items-center gap-4">
        <button
          className="relative p-2 text-slate-400 hover:text-slate-600 transition-colors rounded-full hover:bg-slate-100 focus:outline-none focus-visible:ring-2 focus-visible:ring-indigo-500 focus-visible:ring-offset-1"
          aria-label="Notifications"
          title="Notifications"
        >
          <Bell className="h-5 w-5" aria-hidden="true" />
          <span className="absolute top-1.5 right-1.5 h-2 w-2 rounded-full bg-rose-500 border-2 border-white"></span>
        </button>
        
        <div className="h-6 w-px bg-slate-200 mx-1 hidden sm:block"></div>
        
        <button
          className="flex items-center gap-2 focus:outline-none focus-visible:ring-2 focus-visible:ring-indigo-500 focus-visible:ring-offset-1 rounded-full p-1"
          aria-label="User menu"
          title="User menu"
        >
          <div className="hidden text-right sm:block mr-1">
            <p className="text-sm font-semibold text-slate-700 leading-none">Institute Admin</p>
            <p className="text-xs text-slate-500 mt-1">admin@instareply.ai</p>
          </div>
          <div className="grid h-9 w-9 place-items-center rounded-full bg-gradient-to-br from-indigo-500 to-violet-600 text-sm font-bold text-white shadow-sm ring-2 ring-white hover:ring-indigo-100 transition-all">
            IA
          </div>
        </button>
      </div>
    </header>
  );
}
