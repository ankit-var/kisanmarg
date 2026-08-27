/**
 * Kisaan Marg API Service
 * 
 * Configurable API client for communicating with the future FastAPI backend.
 * Base URL can be configured via environment variable VITE_API_BASE_URL.
 */

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api';

/**
 * Generic API request handler with error handling
 */
async function request(endpoint, options = {}) {
  const url = `${API_BASE_URL}${endpoint}`;
  const config = {
    headers: {
      'Content-Type': 'application/json',
      ...options.headers,
    },
    ...options,
  };

  try {
    const response = await fetch(url, config);
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.message || `HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.warn(`[Kisaan Marg API] Request to ${url} failed:`, error.message);
    throw error;
  }
}

export const apiService = {
  // Base configuration
  getBaseUrl: () => API_BASE_URL,

  /**
   * Health Check
   */
  checkHealth: async () => {
    return request('/health', { method: 'GET' });
  },

  /**
   * Query Mandi prices for a crop and district
   * @param {Object} params - { crop: 'tomato', district: 'Nashik', quantity: 500 }
   */
  getMandiPrices: async (params) => {
    return request('/mandi/prices', {
      method: 'POST',
      body: JSON.stringify(params),
    });
  },

  /**
   * Request AI route & market advice
   * @param {Object} data - { district: 'Nashik', quantity: 500, crop: 'tomato' }
   */
  getAdvice: async (data) => {
    return request('/advice/recommend', {
      method: 'POST',
      body: JSON.stringify(data),
    });
  },

  /**
   * Evaluate a trader offer against regional mandi prices
   * @param {Object} data - { crop: 'tomato', offerPrice: 14, district: 'Nashik' }
   */
  checkTraderOffer: async (data) => {
    return request('/trader/evaluate', {
      method: 'POST',
      body: JSON.stringify(data),
    });
  },

  /**
   * Get bargaining advice/script for negotiation
   * @param {Object} data - { crop: 'tomato', offerPrice: 14, targetPrice: 16 }
   */
  getBargainingAdvice: async (data) => {
    return request('/trader/bargaining-advice', {
      method: 'POST',
      body: JSON.stringify(data),
    });
  },

  /**
   * Set daily alert preference
   * @param {Object} data - { crop: 'tomato', district: 'Nashik', enabled: true }
   */
  setDailyAlert: async (data) => {
    return request('/alerts/subscribe', {
      method: 'POST',
      body: JSON.stringify(data),
    });
  },
};

export default apiService;
