import React from 'react'
import { X, ShieldCheck, Clock, CheckCircle, XCircle, AlertTriangle, Info, Calendar, ExternalLink } from 'lucide-react'

const VERDICT_CONFIG = {
  TRUE: {
    bgColor: 'bg-green-50', borderColor: 'border-green-200', textColor: 'text-green-800',
    iconBg: 'bg-green-100', icon: CheckCircle, label: 'True', description: 'This claim is verified as accurate',
  },
  FALSE: {
    bgColor: 'bg-red-50', borderColor: 'border-red-200', textColor: 'text-red-800',
    iconBg: 'bg-red-100', icon: XCircle, label: 'False', description: 'This claim is verified as false',
  },
  MISLEADING: {
    bgColor: 'bg-amber-50', borderColor: 'border-amber-200', textColor: 'text-amber-800',
    iconBg: 'bg-amber-100', icon: AlertTriangle, label: 'Misleading', description: 'This claim contains misleading information',
  },
  OUTDATED: {
    bgColor: 'bg-purple-50', borderColor: 'border-purple-200', textColor: 'text-purple-800',
    iconBg: 'bg-purple-100', icon: Clock, label: 'Outdated', description: 'This information is no longer current',
  },
  INSUFFICIENT_EVIDENCE: {
    bgColor: 'bg-gray-50', borderColor: 'border-gray-200', textColor: 'text-gray-800',
    iconBg: 'bg-gray-100', icon: Info, label: 'Insufficient Evidence', description: 'Unable to verify with available data',
  },
}

function VerifyResultModal({ result, onClose }) {
  const config = VERDICT_CONFIG[result.verdict] || VERDICT_CONFIG.INSUFFICIENT_EVIDENCE
  const VerdictIcon = config.icon

  const getTruthScoreColor = (score) => {
    if (score >= 70) return 'text-green-600'
    if (score >= 40) return 'text-amber-600'
    return 'text-red-600'
  }

  return (
    <>
      <div className="fixed inset-0 bg-black bg-opacity-60 z-50 animate-backdrop" onClick={onClose} />
      <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
        <div className="bg-white rounded-2xl shadow-2xl w-full max-w-2xl max-h-[90vh] overflow-hidden animate-scale-in" onClick={(e) => e.stopPropagation()}>

          {/* Header */}
          <div className="flex items-center justify-between p-6 border-b border-gray-200">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-gradient-to-br from-purple-600 to-purple-700 rounded-xl flex items-center justify-center">
                <ShieldCheck className="w-6 h-6 text-white" />
              </div>
              <div>
                <h2 className="text-xl font-bold text-gray-900">Fact-Check Result</h2>
                <p className="text-xs text-gray-500">Automated verification analysis</p>
              </div>
            </div>
            <button onClick={onClose} className="p-2 hover:bg-gray-100 rounded-full transition-colors">
              <X className="w-5 h-5 text-gray-600" />
            </button>
          </div>

          {/* Content */}
          <div className="p-6 overflow-y-auto" style={{ maxHeight: 'calc(90vh - 160px)' }}>

            {/* Verdict Badge */}
            <div className={`${config.bgColor} ${config.borderColor} border-2 rounded-2xl p-6 mb-6`}>
              <div className="flex items-start justify-between mb-4">
                <div className="flex items-center space-x-3">
                  <div className={`${config.iconBg} p-3 rounded-xl`}>
                    <VerdictIcon className={`w-6 h-6 ${config.textColor}`} />
                  </div>
                  <div>
                    <h3 className={`text-2xl font-bold ${config.textColor}`}>{config.label}</h3>
                    <p className={`text-sm ${config.textColor} opacity-80`}>{config.description}</p>
                  </div>
                </div>
                <div className="text-right">
                  <div className={`text-3xl font-bold ${getTruthScoreColor(result.truth_score)}`}>
                    {Math.round(result.truth_score)}%
                  </div>
                  <p className="text-xs text-gray-600">Truth Score</p>
                </div>
              </div>
              <div>
                <div className="flex justify-between text-xs text-gray-600 mb-1">
                  <span>Confidence</span><span>{Math.round(result.confidence)}%</span>
                </div>
                <div className="w-full h-2 bg-gray-200 rounded-full overflow-hidden">
                  <div className="h-full bg-gradient-to-r from-purple-600 to-purple-700 transition-all duration-500"
                    style={{ width: `${result.confidence}%` }} />
                </div>
              </div>
            </div>

            {/* Suspicious Claim */}
            <div className="mb-6">
              <h4 className="text-sm font-semibold text-gray-700 mb-2 flex items-center">
                <AlertTriangle className="w-4 h-4 mr-2 text-amber-600" />Suspicious Claim Detected
              </h4>
              <div className="bg-gray-50 border border-gray-200 rounded-xl p-4">
                <p className="text-gray-900 italic">"{result.suspicious_claim}"</p>
              </div>
            </div>

            {/* Verified Fact */}
            <div className="mb-6">
              <h4 className="text-sm font-semibold text-gray-700 mb-2 flex items-center">
                <CheckCircle className="w-4 h-4 mr-2 text-green-600" />Verified Fact
              </h4>
              <div className="bg-green-50 border border-green-200 rounded-xl p-4">
                <p className="text-gray-900">{result.actual_fact}</p>
              </div>
            </div>

            {/* Explanation */}
            <div className="mb-6">
              <h4 className="text-sm font-semibold text-gray-700 mb-2">Explanation</h4>
              <p className="text-gray-700 leading-relaxed">{result.explanation}</p>
            </div>

            {/* Historical Context */}
            {result.historical_context && (
              <div className="mb-6">
                <h4 className="text-sm font-semibold text-gray-700 mb-2 flex items-center">
                  <Clock className="w-4 h-4 mr-2 text-purple-600" />Historical Context
                </h4>
                <div className="bg-purple-50 border border-purple-200 rounded-xl p-4">
                  <p className="text-gray-900">{result.historical_context}</p>
                  {result.was_previously_true && (
                    <div className="mt-3 pt-3 border-t border-purple-200">
                      <p className="text-sm text-purple-800 font-medium">⚠️ This claim was previously true but is now outdated</p>
                    </div>
                  )}
                </div>
              </div>
            )}

            {/* Current Status */}
            <div className="mb-6">
              <h4 className="text-sm font-semibold text-gray-700 mb-2">Current Status</h4>
              <p className="text-gray-700">{result.current_status}</p>
            </div>

            {/* Source Info */}
            <div className="bg-gray-50 border border-gray-200 rounded-xl p-4">
              <h4 className="text-sm font-semibold text-gray-700 mb-3">Source Information</h4>
              <div className="space-y-2">
                <div className="flex items-start">
                  <ExternalLink className="w-4 h-4 mr-2 text-gray-500 mt-0.5 flex-shrink-0" />
                  <div>
                    <p className="text-xs text-gray-600">Source</p>
                    <p className="text-sm font-medium text-gray-900">{result.evidence_source}</p>
                  </div>
                </div>
                {result.source_date && (
                  <div className="flex items-start">
                    <Calendar className="w-4 h-4 mr-2 text-gray-500 mt-0.5 flex-shrink-0" />
                    <div>
                      <p className="text-xs text-gray-600">Last Updated</p>
                      <p className="text-sm font-medium text-gray-900">{result.source_date}</p>
                    </div>
                  </div>
                )}
              </div>
            </div>

            <div className="mt-6 p-4 bg-blue-50 border border-blue-200 rounded-xl">
              <p className="text-xs text-blue-800">
                <span className="font-semibold">Note:</span> This is an automated fact-check based on our verified facts database.
                For critical information, verify through multiple trusted sources.
              </p>
            </div>
          </div>

          {/* Footer */}
          <div className="p-6 border-t border-gray-200 flex items-center justify-between">
            <p className="text-xs text-gray-500">Verified by Fact-Check Social AI</p>
            <button onClick={onClose}
              className="px-6 py-2 bg-gradient-to-r from-purple-600 to-purple-700 text-white rounded-xl hover:from-purple-700 hover:to-purple-800 transition-all shadow-md hover:shadow-lg">
              Close
            </button>
          </div>
        </div>
      </div>
    </>
  )
}

export default VerifyResultModal
