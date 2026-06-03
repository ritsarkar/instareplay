import { DocumentTable } from "@/components/knowledge/DocumentTable";
import { UploadZone } from "@/components/knowledge/UploadZone";
import { BookOpen } from "lucide-react";

export default function KnowledgePage() {
  return (
    <section className="space-y-8">
      <div>
        <div className="flex items-center gap-3 mb-1">
          <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-indigo-100 text-indigo-600">
            <BookOpen className="h-5 w-5" />
          </div>
          <h1 className="text-2xl font-bold tracking-tight text-slate-900">Knowledge Base</h1>
        </div>
        <p className="text-slate-500 max-w-2xl mt-2">
          Upload frequently asked questions, product details, or policy documents. 
          Our AI will instantly read and chunk this data to automatically resolve customer queries.
        </p>
      </div>
      
      <UploadZone />
      
      <div>
        <h2 className="text-lg font-semibold text-slate-900 mb-4">Uploaded Documents</h2>
        <DocumentTable />
      </div>
    </section>
  );
}
