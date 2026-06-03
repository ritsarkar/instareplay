"use client";

import Link from "next/link";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import * as z from "zod";
import { useState } from "react";
import { useRouter } from "next/navigation";
import { CheckCircle2, Chrome } from "lucide-react";
import { api } from "../../../lib/api";
import { useAuthStore } from "../../../store/authStore";

const loginSchema = z.object({
  email: z.string().email("Invalid email address"),
  password: z.string().min(1, "Password is required"),
});

type LoginForm = z.infer<typeof loginSchema>;

export default function LoginPage() {
  const router = useRouter();
  const setAccessToken = useAuthStore((state) => state.setAccessToken);
  const [error, setError] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const { register, handleSubmit, formState: { errors } } = useForm<LoginForm>({
    resolver: zodResolver(loginSchema),
  });

  const onSubmit = async (data: LoginForm) => {
    setIsLoading(true);
    setError("");
    try {
      const formData = new URLSearchParams();
      formData.append("username", data.email);
      formData.append("password", data.password);
      
      const response = await api.post("/auth/login", formData, {
        headers: { "Content-Type": "application/x-www-form-urlencoded" }
      });
      
      setAccessToken(response.data.access_token);
      localStorage.setItem("refresh_token", response.data.refresh_token);
      router.push("/dashboard");
    } catch (err: any) {
      setError(err.response?.data?.detail || "Failed to login. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <main className="grid min-h-screen bg-slate-50 md:grid-cols-2">
      <section className="hidden relative md:flex flex-col justify-between bg-gradient-to-br from-indigo-800 to-indigo-600 p-12 text-white">
        <div>
          <div className="flex items-center gap-2 text-xl font-bold">
            <div className="h-8 w-8 rounded-lg bg-white/20 flex items-center justify-center">
              <span className="text-white">✨</span>
            </div>
            InstaReply AI
          </div>
          <div className="mt-32 max-w-md">
            <h1 className="text-4xl font-bold leading-tight">Automate Instagram replies with confidence.</h1>
            <p className="mt-6 text-lg text-indigo-100">Built for coaching institutes, clinics, real estate teams, and local retailers.</p>
          </div>
        </div>
        <div className="space-y-4 text-indigo-100">
          <div className="flex items-center gap-3">
            <CheckCircle2 className="h-5 w-5 text-emerald-400" />
            <span>24/7 AI-powered instant responses</span>
          </div>
          <div className="flex items-center gap-3">
            <CheckCircle2 className="h-5 w-5 text-emerald-400" />
            <span>Seamless human handoff when needed</span>
          </div>
          <div className="flex items-center gap-3">
            <CheckCircle2 className="h-5 w-5 text-emerald-400" />
            <span>Trained on your custom knowledge base</span>
          </div>
        </div>
      </section>

      <section className="flex items-center justify-center p-6 bg-white">
        <div className="w-full max-w-md space-y-8">
          <div className="text-center md:text-left">
            <h2 className="text-3xl font-bold text-slate-900 tracking-tight">Welcome back</h2>
            <p className="mt-2 text-sm text-slate-500">Sign in to your account to continue.</p>
          </div>

          <button className="flex w-full items-center justify-center gap-2 rounded-lg border border-slate-200 bg-white px-4 py-2.5 text-sm font-medium text-slate-700 shadow-sm transition-all hover:bg-slate-50 hover:text-slate-900 focus:outline-none focus:ring-2 focus:ring-indigo-600 focus:ring-offset-2">
            <Chrome className="h-5 w-5" />
            Continue with Google
          </button>

          <div className="relative">
            <div className="absolute inset-0 flex items-center">
              <div className="w-full border-t border-slate-200"></div>
            </div>
            <div className="relative flex justify-center text-sm">
              <span className="bg-white px-4 text-slate-500">or continue with email</span>
            </div>
          </div>

          <form onSubmit={handleSubmit(onSubmit)} className="space-y-5">
            {error && <div className="rounded-md bg-red-50 p-3 text-sm text-red-600">{error}</div>}
            
            <div className="space-y-1">
              <label className="text-sm font-medium text-slate-700" htmlFor="email">Email</label>
              <input
                {...register("email")}
                id="email"
                className="w-full rounded-md border border-slate-300 px-3 py-2.5 text-sm placeholder-slate-400 shadow-sm focus:border-indigo-600 focus:outline-none focus:ring-1 focus:ring-indigo-600"
                placeholder="name@company.com"
                type="email"
              />
              {errors.email && <p className="text-xs text-red-500">{errors.email.message}</p>}
            </div>

            <div className="space-y-1">
              <label className="text-sm font-medium text-slate-700" htmlFor="password">Password</label>
              <input
                {...register("password")}
                id="password"
                className="w-full rounded-md border border-slate-300 px-3 py-2.5 text-sm placeholder-slate-400 shadow-sm focus:border-indigo-600 focus:outline-none focus:ring-1 focus:ring-indigo-600"
                placeholder="••••••••"
                type="password"
              />
              {errors.password && <p className="text-xs text-red-500">{errors.password.message}</p>}
            </div>

            <button
              disabled={isLoading}
              className="w-full rounded-lg bg-indigo-600 px-4 py-2.5 text-sm font-semibold text-white shadow-sm transition-all hover:bg-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-600 focus:ring-offset-2 disabled:opacity-50"
              type="submit"
            >
              {isLoading ? "Signing in..." : "Login"}
            </button>
          </form>

          <p className="text-center text-sm text-slate-500">
            New here? <Link className="font-semibold text-indigo-600 hover:text-indigo-500 transition-colors" href="/signup">Create an account</Link>
          </p>
        </div>
      </section>
    </main>
  );
}
