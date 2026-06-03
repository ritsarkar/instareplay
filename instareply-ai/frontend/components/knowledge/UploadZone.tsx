"use client";

import { useState } from "react";
import { Plus, X, UploadCloud, Loader2 } from "lucide-react";
import api from "@/lib/api";

export function UploadZone() {
  const [isOpen, setIsOpen] = useState(false);
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!title.trim() || !content.trim()) {
      setError("Both title and content are required.");
      return;
    }
    
    try {
      setIsLoading(true);
      setError("");
      await api.post("/knowledge/upload", { title, content });
      setIsOpen(false);
      setTitle("");
      setContent("");
      // Force a window reload or trigger a callback to refresh the table. 
      // For simplicity in Phase 8, since DocumentTable polls every 5s, it'll show up automatically.
    } catch (err: any) {
      setError(err.response?.data?.detail || "Failed to upload document.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <>
      <div 
        onClick={() => setIsOpen(true)}
        className="group relative cursor-pointer overflow-hidden rounded-2xl border-2 border-dashed border-indigo-200 bg-indigo-50/50 p-10 text-center transition-all hover:border-indigo-400 hover:bg-indigo-50"
      >
        <div className="mx-auto mb-4 flex h-14 w-14 items-center justify-center rounded-full bg-white text-indigo-500 shadow-sm transition-transform group-hover:scale-110 group-hover:text-indigo-600">
          <UploadCloud className="h-7 w-7" />
        </div>
        <p className="text-lg font-semibold text-slate-900">Add Knowledge Document</p>
        <p className="mt-2 text-sm text-slate-500">Paste your FAQs, policies, or product details to train the AI.</p>
        <button className="mt-6 inline-flex items-center gap-2 rounded-lg bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-sm transition-colors hover:bg-indigo-700">
          <Plus className="h-4 w-4" /> Add Text
        </button>
      </div>

      {isOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/50 backdrop-blur-sm p-4">
          <div className="w-full max-w-2xl overflow-hidden rounded-2xl bg-white shadow-2xl">
            <div className="flex items-center justify-between border-b border-slate-100 px-6 py-4">
              <h2 className="text-lg font-bold text-slate-900">Add Text Document</h2>
              <button 
                onClick={() => setIsOpen(false)}
                className="rounded-full p-2 text-slate-400 hover:bg-slate-100 hover:text-slate-600 transition-colors"
              >
                <X className="h-5 w-5" />
              </button>
            </div>
            
            <form onSubmit={handleSubmit} className="p-6">
              {error && (
                <div className="mb-6 rounded-lg bg-rose-50 p-3 text-sm text-rose-600 border border-rose-200">
                  {error}
                </div>
              )}
              
              <div className="mb-6">
                <label htmlFor="title" className="mb-2 block text-sm font-medium text-slate-700">Document Title</label>
                <input
                  type="text"
                  id="title"
                  value={title}
                  onChange={(e) => setTitle(e.target.value)}
                  placeholder="e.g., Shipping Policy 2026"
                  className="w-full rounded-xl border border-slate-200 px-4 py-2.5 text-sm outline-none transition-all focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500"
                  disabled={isLoading}
                />
              </div>
              
              <div className="mb-6">
                <label htmlFor="content" className="mb-2 block text-sm font-medium text-slate-700">Raw Text Content</label>
                <textarea
                  id="content"
                  value={content}
                  onChange={(e) => setContent(e.target.value)}
                  placeholder="Paste your text here..."
                  rows={8}
                  className="w-full resize-y rounded-xl border border-slate-200 px-4 py-3 text-sm outline-none transition-all focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500"
                  disabled={isLoading}
                ></textarea>
                <p className="mt-2 text-xs text-slate-500">The AI will automatically chunk and analyze this content.</p>
              </div>
              
              <div className="flex justify-end gap-3">
                <button
                  type="button"
                  onClick={() => setIsOpen(false)}
                  className="rounded-lg px-4 py-2.5 text-sm font-medium text-slate-600 hover:bg-slate-50 transition-colors"
                  disabled={isLoading}
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  disabled={isLoading}
                  className="inline-flex items-center gap-2 rounded-lg bg-indigo-600 px-5 py-2.5 text-sm font-medium text-white shadow-sm transition-all hover:bg-indigo-700 disabled:opacity-70"
                >
                  {isLoading ? (
                    <>
                      <Loader2 className="h-4 w-4 animate-spin" />
                      Uploading...
                    </>
                  ) : (
                    "Upload Document"
                  )}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </>
  );
}
