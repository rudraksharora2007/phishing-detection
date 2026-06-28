import { Link } from "react-router-dom";
import { motion } from "framer-motion";

const LandingPage = () => (
  <div className="min-h-screen flex items-center justify-center p-6">
    <motion.div initial={{ opacity: 0, y: 24 }} animate={{ opacity: 1, y: 0 }} className="glass max-w-2xl p-10 text-center">
      <h1 className="text-4xl font-bold mb-4">AI-Powered Phishing Detection</h1>
      <p className="text-slate-300 mb-6">Detect phishing links in real time with explainable AI security signals.</p>
      <Link to="/login" className="px-6 py-3 rounded-lg bg-cyber-neon text-black font-semibold">Get Started</Link>
    </motion.div>
  </div>
);

export default LandingPage;
