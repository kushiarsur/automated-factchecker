import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { Shield, LogOut } from 'lucide-react'
import { getUser, logout } from '../utils/auth'
import { logoutAPI } from '../services/api'

function Header() {
  const navigate = useNavigate()
  const user = getUser()
  const [showUserMenu, setShowUserMenu] = useState(false)

  const handleLogout = async () => {
    try { await logoutAPI() } catch (e) { console.error(e) }
    logout()
    navigate('/login')
  }

  return (
    <header className="bg-white border-b border-gray-200 sticky top-0 z-50 shadow-sm">
      <div className="max-w-6xl mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center space-x-3">
            <div className="w-10 h-10 bg-gradient-to-br from-purple-600 to-purple-700 rounded-xl flex items-center justify-center shadow-md">
              <Shield className="w-6 h-6 text-white" />
            </div>
            <div>
              <h1 className="text-xl font-bold gradient-text">Fact-Check Social</h1>
              <p className="text-xs text-gray-500">Verify before you share</p>
            </div>
          </div>

          <div className="relative">
            <button onClick={() => setShowUserMenu(!showUserMenu)}
              className="flex items-center space-x-2 px-3 py-2 rounded-xl hover:bg-gray-100 transition-colors">
              <img
                src={user?.avatar_url || `https://ui-avatars.com/api/?name=User&background=9333ea&color=fff`}
                alt={user?.username || 'User'}
                className="w-8 h-8 rounded-full ring-2 ring-purple-200"
              />
              <span className="text-sm font-medium text-gray-700 hidden sm:block">{user?.username || 'User'}</span>
            </button>

            {showUserMenu && (
              <>
                <div className="fixed inset-0 z-40" onClick={() => setShowUserMenu(false)} />
                <div className="absolute right-0 mt-2 w-56 bg-white rounded-xl shadow-xl border border-gray-200 py-2 z-50 animate-scale-in">
                  <div className="px-4 py-3 border-b border-gray-100">
                    <p className="text-sm font-semibold text-gray-900">{user?.username}</p>
                    <p className="text-xs text-gray-500 mt-0.5">{user?.email}</p>
                  </div>
                  <button onClick={handleLogout}
                    className="w-full px-4 py-2 text-left text-sm text-red-600 hover:bg-red-50 flex items-center space-x-2 transition-colors">
                    <LogOut className="w-4 h-4" />
                    <span>Log out</span>
                  </button>
                </div>
              </>
            )}
          </div>
        </div>
      </div>
    </header>
  )
}

export default Header
