"use client";

import { useEffect, useState } from "react";
import { FileText, Loader2, CheckCircle2, AlertCircle, Trash2 } from "lucide-react";
import api from "@/lib/api";

interface KnowledgeDoc {
  id: string;
  title: string;
  status: string;
  chunk_count: number;
  created_at: string;
}

export function DocumentTable() {
  const [documents, setDocuments] = useState<KnowledgeDoc[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  const fetchDocuments = async () => {
    try {
      const response = await api.get("/knowledge");
      setDocuments(response.data);
    } catch (error) {
      console.error("Failed to fetch documents", error);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchDocuments();
    
    // Poll every 5 seconds to update status
    const interval = setInterval(fetchDocuments, 5000);
    return () => clearInterval(interval);
  }, []);

  if (isLoading) {
    return (
      <div className="flex h-32 items-center justify-center rounded-xl border border-slate-200 bg-white">
        <Loader2 className="h-6 w-6 animate-spin text-indigo-500" />
      </div>
    );
  }

  return (
    <section className="overflow-hidden rounded-xl border border-slate-200 bg-white shadow-sm">
      <div className="grid grid-cols-12 gap-4 border-b border-slate-200 bg-slate-50/50 px-6 py-4 text-xs font-bold uppercase tracking-wider text-slate-500">
        <div className="col-span-5">Name</div>
        <div className="col-span-2">Chunks</div>
        <div className="col-span-3">Status</div>
        <div className="col-span-2 text-right">Actions</div>
      </div>
      
      <div className="divide-y divide-slate-100">
        {documents.length === 0 ? (
          <div className="px-6 py-12 text-center text-sm text-slate-500">
            No knowledge documents uploaded yet. Add one above.
          </div>
        ) : (
          documents.map((doc) => (
            <div key={doc.id} className="grid grid-cols-12 items-center gap-4 px-6 py-4 transition-colors hover:bg-slate-50/80">
              <div className="col-span-5 flex items-center gap-3">
                <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-50 text-indigo-600">
                  <FileText className="h-5 w-5" />
                </div>
                <div>
                  <p className="font-semibold text-slate-900">{doc.title}</p>
                  <p className="text-xs text-slate-500">{new Date(doc.created_at).toLocaleDateString()}</p>
                </div>
              </div>
              
              <div className="col-span-2">
                <span className="inline-flex items-center rounded-md bg-slate-100 px-2 py-1 text-xs font-medium text-slate-600 ring-1 ring-inset ring-slate-500/10">
                  {doc.chunk_count} chunks
                </span>
              </div>
              
              <div className="col-span-3">
                {doc.status === "processing" ? (
                  <div className="flex items-center gap-2 text-sm font-medium text-amber-600">
                    <Loader2 className="h-4 w-4 animate-spin" /> Processing
                  </div>
                ) : doc.status === "ready" ? (
                  <div className="flex items-center gap-2 text-sm font-medium text-emerald-600">
                    <CheckCircle2 className="h-4 w-4" /> Ready
                  </div>
                ) : (
                  <div className="flex items-center gap-2 text-sm font-medium text-rose-600">
                    <AlertCircle className="h-4 w-4" /> Failed
                  </div>
                )}
              </div>
              
              <div className="col-span-2 flex justify-end">
                <button
                  type="button"
                  aria-label={`Delete ${doc.title}`}
                  title={`Delete ${doc.title}`}
                  className="rounded-lg p-2 text-slate-400 hover:bg-rose-50 hover:text-rose-600 transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-indigo-500 focus-visible:ring-offset-1"
                >
                  <Trash2 aria-hidden="true" className="h-4 w-4" />
                </button>
              </div>
            </div>
          ))
        )}
      </div>
    </section>
  );
}
