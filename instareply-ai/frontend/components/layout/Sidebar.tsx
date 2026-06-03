"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { 
  LayoutDashboard, 
  MessageSquare, 
  Users, 
  BookOpen, 
  BarChart3, 
  Settings, 
  CreditCard 
} from "lucide-react";

const navItems = [
  { href: "/dashboard", label: "Dashboard", icon: LayoutDashboard },
  { href: "/inbox", label: "Inbox", icon: MessageSquare },
  { href: "/customers", label: "Customers", icon: Users },
  { href: "/knowledge", label: "Knowledge", icon: BookOpen },
  { href: "/analytics", label: "Analytics", icon: BarChart3 },
  { href: "/settings", label: "Settings", icon: Settings },
  { href: "/billing", label: "Billing", icon: CreditCard },
];

export function Sidebar() {
  const pathname = usePathname();

  return (
    <aside className="fixed inset-y-0 left-0 hidden w-[260px] bg-indigo-950 p-5 text-indigo-100 md:flex md:flex-col shadow-xl z-30">
      <div className="flex items-center gap-3 mb-10 px-2">
        <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-indigo-500/20 border border-indigo-400/30">
          <span className="text-xl">✨</span>
        </div>
        <Link className="text-xl font-bold tracking-tight text-white hover:opacity-90 transition-opacity" href="/dashboard">
          InstaReply <span className="text-indigo-400">AI</span>
        </Link>
      </div>
      
      <nav className="space-y-1.5 flex-1">
        {navItems.map((item) => {
          const isActive = pathname === item.href || pathname?.startsWith(`${item.href}/`);
          const Icon = item.icon;
          
          return (
            <Link 
              key={item.href}
              href={item.href} 
              className={`group flex items-center gap-3 rounded-lg px-3 py-2.5 text-sm font-medium transition-all duration-200 ${
                isActive 
                  ? "bg-indigo-600 text-white shadow-md shadow-indigo-900/50" 
                  : "text-indigo-200 hover:bg-white/10 hover:text-white"
              }`}
            >
              <Icon className={`h-5 w-5 transition-colors ${isActive ? "text-indigo-100" : "text-indigo-400 group-hover:text-indigo-200"}`} />
              {item.label}
            </Link>
          );
        })}
      </nav>
      
      <div className="mt-auto px-2">
        <div className="rounded-xl bg-indigo-900/50 p-4 border border-indigo-800/50">
          <p className="text-xs font-medium text-indigo-300 uppercase tracking-wider mb-2">Beta Access</p>
          <p className="text-sm text-indigo-100 mb-3">You are using the Bengaluru-first beta version.</p>
          <div className="h-1.5 w-full bg-indigo-950 rounded-full overflow-hidden">
            <div className="h-full bg-emerald-400 w-full rounded-full"></div>
          </div>
        </div>
      </div>
    </aside>
  );
}
