import React from 'react'
import { Loader2 } from 'lucide-react'

function LoadingSpinner({ size = 'medium', text = '' }) {
  const sizeClasses = { small: 'w-4 h-4', medium: 'w-8 h-8', large: 'w-12 h-12' }
  return (
    <div className="flex flex-col items-center justify-center">
      <Loader2 className={`${sizeClasses[size]} text-purple-600 animate-spin`} />
      {text && <p className="mt-3 text-sm text-gray-600">{text}</p>}
    </div>
  )
}

export default LoadingSpinner
